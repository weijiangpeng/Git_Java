package com.ego.dubbo.service.impl;

import java.util.List;

import javax.annotation.Resource;

import com.ego.commons.pojo.EasyUIDataGrid;
import com.ego.dubbo.service.TbItemDubboService;
import com.ego.mapper.TbItemDescMapper;
import com.ego.mapper.TbItemMapper;
import com.ego.mapper.TbItemParamItemMapper;
import com.ego.pojo.TbItem;
import com.ego.pojo.TbItemDesc;
import com.ego.pojo.TbItemExample;
import com.ego.pojo.TbItemParamItem;
import com.github.pagehelper.PageHelper;
import com.github.pagehelper.PageInfo;

public class TbItemDubboServiceImpl implements TbItemDubboService {
	@Resource
	private TbItemMapper tbItemMapper;
	@Resource
	private TbItemDescMapper TbItemDescMapper;
	@Resource
	private TbItemParamItemMapper tbItemParamItemMapper;

	@Override
	public EasyUIDataGrid show(int page, int rows) {
		
		PageHelper.startPage(page,rows);
		//查询全部
		List<TbItem> list= tbItemMapper.selectByExample(new TbItemExample());
		//分页代码
		PageInfo<TbItem> pi=new PageInfo<TbItem>(list);
		//设置分页条件
		//放入实体类
		EasyUIDataGrid datagrid=new EasyUIDataGrid();
		datagrid.setRows(pi.getList());
		datagrid.setTotal(pi.getTotal());
		return datagrid;
	}

	@Override
	public int updItemStatus(TbItem tbItem) {
		// TODO Auto-generated method stub
		return tbItemMapper.updateByPrimaryKeySelective(tbItem);
	}

	@Override
	public int insTbItem(TbItem tbItem) {
		// TODO Auto-generated method stub
		return 0;
	}

	@Override
	public int insTbItemDesc(TbItem tbItem, TbItemDesc desc,TbItemParamItem paramItem) throws Exception {
		// TODO Auto-generated method stub
		int index=0;
		try {
			index+=tbItemMapper.insertSelective(tbItem);
			index+=TbItemDescMapper.insertSelective(desc);
			index+=tbItemParamItemMapper.insertSelective(paramItem);
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		if(index==3) {
			return 1;
		}else {
			throw new Exception("新增失败，数据还原");
		}
	}

	@Override
	public List<TbItem> selAllByStatus(byte status) {
		TbItemExample example = new TbItemExample();
		example.createCriteria().andStatusEqualTo(status);
		return tbItemMapper.selectByExample(example);
	}

	@Override
	public TbItem selById(Long id) {
		// TODO Auto-generated method stub
		return tbItemMapper.selectByPrimaryKey(id);
	}
	
}
