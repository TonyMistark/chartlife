from django.shortcuts import render

# Create your views here.
from jinja2 import Environment, FileSystemLoader
from pyecharts.globals import CurrentConfig
from django.http import HttpResponse
from rest_framework import permissions

CurrentConfig.GLOBAL_ENV = Environment(loader=FileSystemLoader("./consumption/templates"))

from pyecharts import options as opts
from pyecharts.charts import Bar, Radar
from common.view import BaseView


def index(request):
    c = (
        Bar()
        .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
        .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
        .add_yaxis("商家B", [15, 25, 16, 55, 48, 8])
        .set_global_opts(title_opts=opts.TitleOpts(title="Bar-基本示例", subtitle="我是副标题"))
    )
    return HttpResponse(c.render_embed())


def index2(request):
    c = (
        Bar()
            .add_xaxis(["01月", "02月", "03月", "04月", "05月", "06月", "07月", "08月"])
            .add_yaxis("养老保险", [5, 20, 5, 20, 20, 5, 20, 5, ])
            .add_yaxis("医疗保险", [15, 25, 15, 25, 15, 25, 15, 25, ])
            .add_yaxis("失业保险", [16, 88, 16, 88, 16, 88, 16, 88, ])
            .add_yaxis("工伤保险", [17, 88, 17, 88, 17, 88, 17, 88, ])
            .add_yaxis("生育保险", [17, 25, 17, 25, 17, 25, 17, 25, ])
            .add_yaxis("公积金", [15, 25, 15, 25, 15, 25, 15, 25,])
            .set_global_opts(title_opts=opts.TitleOpts(title="五险一金", subtitle="月份"))
    )
    return HttpResponse(c.render_embed())


def radar(request):
    v1 = [[4300, 10000, 28000, 35000, 50000, 19000]]
    v2 = [[5000, 14000, 28000, 31000, 42000, 21000]]
    c = (
        Radar()
        .add_schema(
            schema=[
                opts.RadarIndicatorItem(name="养老保险", max_=6500),
                opts.RadarIndicatorItem(name="医疗保险", max_=16000),
                opts.RadarIndicatorItem(name="失业保险", max_=30000),
                opts.RadarIndicatorItem(name="工伤保险", max_=38000),
                opts.RadarIndicatorItem(name="生育保险", max_=52000),
                opts.RadarIndicatorItem(name="公积金", max_=25000),
            ]
        )
        .add("预算分配", v1)
        .add("实际开销", v2)
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
            legend_opts=opts.LegendOpts(selected_mode="single"),
            title_opts=opts.TitleOpts(title="Radar-单例模式"),
        )
    )
    return HttpResponse(c.render_embed())




class BillView(BaseView):
    permission_classes = (permissions.AllowAny, )

    def get(self, request):
        c = (
            Bar()
                .add_xaxis(["08月", "07月"])
                .add_yaxis("养老保险", [5, 20])
                .add_yaxis("医疗保险", [15, 25])
                .add_yaxis("失业保险", [16, 88])
                .add_yaxis("工伤保险", [17, 88])
                .add_yaxis("生育保险", [17, 25])
                .add_yaxis("公积金", [15, 25])
                .set_global_opts(title_opts=opts.TitleOpts(title="五险一金", subtitle="月份"))
        )
        return HttpResponse(c.render_embed())
