<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Insert title here</title>
<script type="text/javascript" src=""js/jquery-1.7.2.js""></script>
<script type="text/javascript">
$(function(){
	$("a").click(function(){
		$("img").attr("src","validCode?date="+new Date());
		return false;
	})
})
</script>
</head>
<body>
<form action="login" method="post">
	用户名:<input type="text" name="username" /><br/>
	密码:<input type="password" name="password" /><br/>
	验证码:<input type="text" size="1" name="code" /><img  src="validCode" width="50" height="25"><a href="" >看不清</a><br/>
	<input type="submit" value="登录" /><input type="reset" value="重置" />
</form>
</body>
</html>