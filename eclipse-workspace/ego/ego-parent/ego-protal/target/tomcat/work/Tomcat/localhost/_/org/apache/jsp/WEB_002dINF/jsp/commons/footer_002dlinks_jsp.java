/*
 * Generated by the Jasper component of Apache Tomcat
 * Version: Apache Tomcat/7.0.47
 * Generated at: 2020-05-06 15:28:03 UTC
 * Note: The last modified time of this file was set to
 *       the last modified time of the source file after
 *       generation to assist with modification tracking.
 */
package org.apache.jsp.WEB_002dINF.jsp.commons;

import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.jsp.*;

public final class footer_002dlinks_jsp extends org.apache.jasper.runtime.HttpJspBase
    implements org.apache.jasper.runtime.JspSourceDependent {

  private static final javax.servlet.jsp.JspFactory _jspxFactory =
          javax.servlet.jsp.JspFactory.getDefaultFactory();

  private static java.util.Map<java.lang.String,java.lang.Long> _jspx_dependants;

  private javax.el.ExpressionFactory _el_expressionfactory;
  private org.apache.tomcat.InstanceManager _jsp_instancemanager;

  public java.util.Map<java.lang.String,java.lang.Long> getDependants() {
    return _jspx_dependants;
  }

  public void _jspInit() {
    _el_expressionfactory = _jspxFactory.getJspApplicationContext(getServletConfig().getServletContext()).getExpressionFactory();
    _jsp_instancemanager = org.apache.jasper.runtime.InstanceManagerFactory.getInstanceManager(getServletConfig());
  }

  public void _jspDestroy() {
  }

  public void _jspService(final javax.servlet.http.HttpServletRequest request, final javax.servlet.http.HttpServletResponse response)
        throws java.io.IOException, javax.servlet.ServletException {

    final javax.servlet.jsp.PageContext pageContext;
    javax.servlet.http.HttpSession session = null;
    final javax.servlet.ServletContext application;
    final javax.servlet.ServletConfig config;
    javax.servlet.jsp.JspWriter out = null;
    final java.lang.Object page = this;
    javax.servlet.jsp.JspWriter _jspx_out = null;
    javax.servlet.jsp.PageContext _jspx_page_context = null;


    try {
      response.setContentType("text/html; charset=UTF-8");
      pageContext = _jspxFactory.getPageContext(this, request, response,
      			null, true, 8192, true);
      _jspx_page_context = pageContext;
      application = pageContext.getServletContext();
      config = pageContext.getServletConfig();
      session = pageContext.getSession();
      out = pageContext.getOut();
      _jspx_out = out;

      out.write("\r\n");
      out.write("<div id=\"footer-2013\">\r\n");
      out.write("\t<div class=\"links\"><a href=\"http://www.jd.com/intro/about.aspx\" target=\"_blank\" rel=\"nofollow\">关于我们</a>|<a href=\"http://www.jd.com/contact/\" target=\"_blank\" rel=\"nofollow\">联系我们</a>|<a href=\"http://zhaopin.jd.com/\" target=\"_blank\" rel=\"nofollow\">人才招聘</a>|<a href=\"http://www.jd.com/contact/joinin.aspx\" target=\"_blank\" rel=\"nofollow\">商家入驻</a>|<a href=\"http://jzt.jd.com\" target=\"_blank\" rel=\"nofollow\">营销中心</a>|<a href=\"http://app.jd.com/\" target=\"_blank\" rel=\"nofollow\">手机易购</a>|<a href=\"http://club.jd.com/links.aspx\" target=\"_blank\">友情链接</a>|<a href=\"http://media.jd.com/\" target=\"_blank\">销售联盟</a>|<a target=\"_blank\" href=\"http://club.jd.com/\">易购社区</a>|<a target=\"_blank\" href=\"http://gongyi.jd.com\">易购公益</a>|<a target=\"_blank\" href=\"http://en.jd.com/\">English Site</a></div>\r\n");
      out.write("</div>");
    } catch (java.lang.Throwable t) {
      if (!(t instanceof javax.servlet.jsp.SkipPageException)){
        out = _jspx_out;
        if (out != null && out.getBufferSize() != 0)
          try { out.clearBuffer(); } catch (java.io.IOException e) {}
        if (_jspx_page_context != null) _jspx_page_context.handlePageException(t);
        else throw new ServletException(t);
      }
    } finally {
      _jspxFactory.releasePageContext(_jspx_page_context);
    }
  }
}
