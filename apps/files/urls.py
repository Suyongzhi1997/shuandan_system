from django.urls import path, re_path
# 要写上app的名字
from django.views.generic import TemplateView
from .views import UploadExcelView, DownloadAllInfoView, DownloadAllRecordExcelView, DownloadExcelView, SdgsDownloadView, DownloadTemplateView, UploadDirectReviewFileView, DownloadBrushMoneyExcelView, UploadCheckExcelView, DownloadInfoView, UploadDeliveryExcelView
app_name = "file"

urlpatterns = [
    # 提交刷单记录
    path('upload/', UploadExcelView.as_view(), name="upload_excel"),
    # 上传直评文件
    path('upload/direct_review_file/', UploadDirectReviewFileView.as_view(), name="upload_direct_review_file"),
    # 提交审核刷单记录
    path('upload/check/', UploadCheckExcelView.as_view(), name="upload_check_excel"),
    # 提交物流信息
    path('upload/delivery/', UploadDeliveryExcelView.as_view(), name="upload_delivery_excel"),
    path('download/', DownloadExcelView.as_view(), name="download_excel"),
    # 下载所有刷单信息
    path('download/all_record/', DownloadAllRecordExcelView.as_view(), name="download_all_record_excel"),
    # 下载刷单金额
    path('download/brush_money/', DownloadBrushMoneyExcelView.as_view(), name="download_brush_money_excel"),
    # 下载物流信息
    path('download/info/', DownloadInfoView.as_view(), name="download_info_excel"),
    # 下载全部物流信息
    path('download/all_info/', DownloadAllInfoView.as_view(), name="download_all_info_excel"),
    # 下载模板文件
    path('download/template/', DownloadTemplateView.as_view()),
    # 刷單公司下載文件
    path('sdgs_download/', SdgsDownloadView.as_view())
]
