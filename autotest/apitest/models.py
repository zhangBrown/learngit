from django.db import models


# Create your models here.
class Apitest(models.Model):
    """业务场景接口"""
    Product = models.ForeignKey('product.Product', on_delete=models.CASCADE, null=True)
    apitest_name = models.CharField('流程接口名称', max_length=64)
    apitest_desc = models.CharField('流程接口描述', max_length=128, null=True)
    apitester = models.CharField('测试负责人', max_length=16)
    apitest_result = models.BooleanField('测试结果')
    create_time = models.DateTimeField('创建时间', auto_now=True)

    class Meta:
        verbose_name = '流程场景接口'
        verbose_name_plural = '流程场景接口'

    def __str__(self):
        return self.apitest_name


class Apistep(models.Model):
    """单接口步骤"""
    Apitest = models.ForeignKey(Apitest, on_delete=models.CASCADE)
    api_name = models.CharField('接口名称', max_length=100)
    api_url = models.CharField('接口url', max_length=200)
    api_step = models.CharField('接口步骤', max_length=100, null=True)
    api_param = models.CharField('接口参数和值', max_length=800)
    REQUEST_METHOD = (('get', "get"), ('post', 'post'), ('put', 'put'))
    api_method = models.CharField(verbose_name='请求方法', choices=REQUEST_METHOD,
                                  default='get', max_length=200, null=True)
    api_except_result = models.CharField('预期结果', max_length=200)
    api_response = models.CharField('响应数据', max_length=5000, null=True)
    api_status = models.BooleanField('是否通过')
    create_time = models.DateTimeField('创建时间', auto_now=True)

    def __str__(self):
        return self.api_name


class Apis(models.Model):
    Product = models.ForeignKey("product.Product", on_delete=models.CASCADE, null=True)
    api_name = models.CharField("接口名称", max_length=100)
    api_url = models.CharField("接口url", max_length=200)
    api_param = models.CharField("接口参数和值", max_length=800)
    REQUEST_METHOD = (("0", "get"), ("1", "post"), ("2", "put"))
    api_method = models.CharField(verbose_name="请求方法", choices=REQUEST_METHOD, default="0", max_length=200)
    api_except = models.CharField("预期结果", max_length=200)
    api_status = models.BooleanField("是否通过")
    create_time = models.DateTimeField("创建时间", auto_now=True)

    class META:
        verbose_name = "单一接口"
        verbose_name_plural = "单一接口"

    def __str__(self):
        return self.api_name
