import os
import matplotlib.pyplot as plt
from torch.utils.data import DataLoader
import torch
from Multi_Network import *
from torchvision.transforms import transforms
from PIL import Image
import pandas as pd
import random
from torch import optim
from torch.optim import lr_scheduler
import copy

ROOT_DIR = '../Dataset/'
TRAIN_DIR = 'train/'
VAL_DIR = 'val/'
TRAIN_ANNO = 'Multi_train_annotation.csv'
VAL_ANNO = 'Multi_val_annotation.csv'
CLASSES = ['Mammals', 'Birds']
SPECIES = ['rabbits', 'rats', 'chickens']

save_name = 'best_model_2.pt'
img1_name = 'train and val loss vs epoches 2.jpg'
img2_name = 'train and val Species acc vs epoches 2.jpg'

class MyDataset():

    def __init__(self, root_dir, annotations_file, transform=None):

        self.root_dir = root_dir
        self.annotations_file = annotations_file
        self.transform = transform

        if not os.path.isfile(self.annotations_file):
            print(self.annotations_file + 'does not exist!')
        self.file_info = pd.read_csv(annotations_file, index_col=0)
        self.size = len(self.file_info)

    def __len__(self):
        return self.size

    def __getitem__(self, idx):
        image_path = self.file_info['path'][idx]
        if not os.path.isfile(image_path):
            print(image_path + '  does not exist!')
            return None

        image = Image.open(image_path).convert('RGB')
        label_species = int(self.file_info.iloc[idx]['species'])
        label_classes = int(self.file_info.iloc[idx]['classes'])

        sample = {'image': image, 'species': label_species, 'classes':label_classes}
        if self.transform:
            sample['image'] = self.transform(image)
        return sample

train_transforms = transforms.Compose([transforms.Resize((500, 500)),
                                       transforms.RandomHorizontalFlip(),
                                       transforms.ToTensor(),
                                       ])
val_transforms = transforms.Compose([transforms.Resize((500, 500)),
                                     transforms.ToTensor()
                                     ])

train_dataset = MyDataset(root_dir= ROOT_DIR + TRAIN_DIR,
                          annotations_file= TRAIN_ANNO,
                          transform=train_transforms)

test_dataset = MyDataset(root_dir= ROOT_DIR + VAL_DIR,
                         annotations_file= VAL_ANNO,
                         transform=val_transforms)

train_loader = DataLoader(dataset=train_dataset, batch_size=128 , shuffle=True)
test_loader = DataLoader(dataset=test_dataset)
data_loaders = {'train': train_loader, 'val': test_loader}

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
print(device)

# def visualize_dataset():
#     print(len(train_dataset))
#     idx = random.randint(0, len(train_dataset))
#     sample = train_loader.dataset[idx]
#     print(idx, sample['image'].shape, SPECIES[sample['species']], CLASSES[sample['classes']])
#     img = sample['image']
#     plt.imshow(transforms.ToPILImage()(img))
#     plt.show()
# visualize_dataset()

def train_model(model, criterion, optimizer, scheduler, num_epochs=50):
    Loss_list = {'train': [], 'val': []}
    Accuracy_list_species = {'train': [], 'val': []}

    best_model_wts = copy.deepcopy(model.state_dict())
    best_acc = 0.0

    for epoch in range(num_epochs):
        print('Epoch {}/{}'.format(epoch, num_epochs - 1))
        print('-*' * 10)

        # Each epoch has a training and validation phase
        for phase in ['train', 'val']:
            if phase == 'train':
                model.train()
            else:
                model.eval()

            running_loss = 0.0
            corrects_example = 0

            for idx,data in enumerate(data_loaders[phase]):
                #print(phase+' processing: {}th batch.'.format(idx))
                inputs = data['image'].to(device)
                labels_species = data['species'].to(device)
                labels_classes = data['classes'].to(device)
                labels_example = labels_species+labels_classes
                optimizer.zero_grad()

                with torch.set_grad_enabled(phase == 'train'):
                    x_species, x_classes = model(inputs)
                    x_classes = x_classes.view(-1,2)
                    x_species = x_species.view(-1,3)

                    _, preds_species = torch.max(x_species, 1)
                    _, preds_classes = torch.max(x_classes, 1)
                    preds_example = preds_species+preds_classes

                    loss_1 = criterion(x_species, labels_species)
                    loss_2 = criterion(x_classes, labels_classes)

                    if phase == 'train':
                        loss_1.backward(retain_graph=True)
                        loss_2.backward()
                        optimizer.step()

                running_loss += (0.5*loss_1.item()+0.5*loss_2.item()) * inputs.size(0)

                corrects_example += torch.sum(preds_example == labels_example)

            epoch_loss = running_loss / len(data_loaders[phase].dataset)
            Loss_list[phase].append(epoch_loss)

            epoch_acc_example = corrects_example.double() / len(data_loaders[phase].dataset)
            epoch_acc = epoch_acc_example

            Accuracy_list_species[phase].append(100 * epoch_acc_example)
            print('{} Loss: {:.4f}  Acc_example: {:.2%}'.format(phase, epoch_loss,epoch_acc_example))

            if phase == 'val' and epoch_acc > best_acc:

                best_acc = epoch_acc_example
                best_model_wts = copy.deepcopy(model.state_dict())
                print('Best val example Acc: {:.2%}'.format(best_acc))

    model.load_state_dict(best_model_wts)
    torch.save(model.state_dict(), save_name)
    print('Best val example Acc: {:.2%}'.format(best_acc))
    return model, Loss_list,Accuracy_list_species

network = Net().to(device)
optimizer = optim.SGD(network.parameters(), lr=0.01, momentum=0.9)
criterion = nn.CrossEntropyLoss()
exp_lr_scheduler = lr_scheduler.StepLR(optimizer, step_size=1, gamma=0.05) # Decay LR by a factor of 0.1 every 1 epochs
model, Loss_list, Accuracy_list_species = train_model(network, criterion, optimizer, exp_lr_scheduler, num_epochs=30)

x = range(len(Loss_list["train"]))
y1 = Loss_list["val"]
y2 = Loss_list["train"]

plt.plot(x, y1, color="r", linestyle="-", marker="o", linewidth=1, label="val")
plt.plot(x, y2, color="b", linestyle="-", marker="o", linewidth=1, label="train")
plt.legend()
plt.title('train and val loss vs. epoches')
plt.ylabel('loss')
plt.savefig(img1_name)
plt.close('all') # 关闭图 0

y5 = Accuracy_list_species["train"]
y6 = Accuracy_list_species["val"]
plt.plot(x, y5, color="r", linestyle="-", marker=".", linewidth=1, label="train")
plt.plot(x, y6, color="b", linestyle="-", marker=".", linewidth=1, label="val")
plt.legend()
plt.title('train and val Example acc vs. epoches')
plt.ylabel('Example accuracy') 
plt.savefig(img2_name)
plt.close('all')

# ######################################## Visualization ##################################
def visualize_model(model):
    model.eval()
    with torch.no_grad():
    	error_example = {'num':0, 'example':[]}
    	for i, data in enumerate(data_loaders['val']):
            inputs = data['image']
            labels_species = data['species'].to(device)
            labels_classes = data['classes'].to(device)

            x_species, x_classes = model(inputs.to(device))
            x_species = x_species.view( -1,3)
            x_classes = x_classes.view(-1, 2)

            _, preds_species = torch.max(x_species, 1)
            _, preds_classes = torch.max(x_classes, 1)
            preds_example = preds_species+preds_classes

            if SPECIES[preds_species] != SPECIES[labels_species] or CLASSES[preds_classes] != CLASSES[labels_classes] :
            	error_example['num'] += 1
            	error_example['example'].append([data['image'], SPECIES[preds_species], SPECIES[labels_species], CLASSES[preds_classes], CLASSES[labels_classes]])
    print(error_example['num'], data_loaders['val'].__len__())
    print("val_acc:{:.2f}%".format((1-error_example['num']/data_loaders['val'].__len__())*100))
    # for img in error_example['example']:
    # 	plt.imshow(transforms.ToPILImage()(img[0].squeeze(0)))
    # 	plt.title('predicted species: {}\n ground-truth species:{}\n predicted classes{}\n ground-truth classes{}  '.format(img[1], img[2], img[3], img[4]))
    # 	plt.show()

network = Net().to(device)
state_dict_load = torch.load(save_name)
network.load_state_dict(state_dict_load)

visualize_model(network)