from django.urls import path, re_path
from .views import OperationEditView, SubmitCheckView, ShCheckView, SdBrushRecordsView, ShResetChecksView, \
    ShResetCheckView, ShSumBrushMoneyView, ShAlreadyCheckRecordsView, ShSubmitCheckView, YySubmitBrushView, \
    ShCheckRecordsView, YyAlreadyCheckRecordsView, YyCheckRecordsView, YyWaitCheckRecordsView, EditCheckView, \
    UploadImageView, YyFeedBackView, DeleteRecordView, FeedBackUnFavoriteRecordView, \
    FeedBackRecordsView, FeedBackView, FeedBackFavoriteRecordView, \
    SdBrushEditView, SdSubmitBrushView, SdAlreadyCheckRecords, SdResetCheck, SdResetChecks, SdgsBrushRecordsView, \
    SdgsBrushEdit, YyResetCommitView, YyBrushMoneyView, ShBrushMoneyView, ShSumBrushMoneyView, SdSearchRecords, \
    ShSearchRecords, ShResetBrush, YyDirectReviewEditView, Sdgs403View, ShSdgsBrushEdit, YyFeedbackRecordEditView, \
    ShDeleteRecordsView, ShReturnCheckView, AddCheckView
# 要写上app的名字
from django.views.generic import TemplateView

app_name = "record"

urlpatterns = [
    # 编辑
    path('edit/', OperationEditView.as_view(), name="operation_edit_record"),
    # 更换产品图片
    path('upload_image/', UploadImageView.as_view(), name="upload_image"),
    # 删除记录
    path('delete_record/', DeleteRecordView.as_view(), name="delete_record"),
    # # 收藏
    # path('favorite/', FavoriteRecordView.as_view(), name="favorite_record"),
    # # 取消收藏
    # path('unfavorite/', UnFavoriteRecordView.as_view(), name="unfavorite_record"),
    # 反馈收藏动作
    path('favorite/fb/', FeedBackFavoriteRecordView.as_view(), name="favorite_fb_records"),
    # 反馈取消收藏动作
    path('unfavorite/fb/', FeedBackUnFavoriteRecordView.as_view(), name="unfavorite_fb_records"),
    # 反馈页面
    path('feedback/', FeedBackView.as_view(), name="feedback"),
    # 反馈收藏页面
    path('favorite/fb/records/', FeedBackRecordsView.as_view(), name="feedback_records"),

    # 运营
    # 添加
    path('yy/add/check/', AddCheckView.as_view(), name="yy_add_check"),
    # 运营审核提交页面
    path('yy/check/records/', YyCheckRecordsView.as_view(), name="yy_check_records"),
    # 审核编辑
    path('yy/edit/check/', EditCheckView.as_view(), name="edit_check"),
    # 提交审核
    path('yy/submit/check/', SubmitCheckView.as_view(), name="submit_check"),
    # 等待审核
    path('yy/wait/check/records/', YyWaitCheckRecordsView.as_view(), name="yy_wait_check_records"),
    # 已审核
    path('yy/already/check/records/', YyAlreadyCheckRecordsView.as_view(), name="yy_already_check_records"),
    # 刷单提交
    path('yy/submit/brush/', YySubmitBrushView.as_view(), name="submit_brush"),
    # 运营反馈页面
    path('yy/feedback/', YyFeedBackView.as_view(), name="yy_feedback"),
    # 运营重新提交
    path('yy/reset/commit', YyResetCommitView.as_view(), name="yy_reset_commit"),
    # 运营刷单费用
    path('yy/brush_money/', YyBrushMoneyView.as_view(), name="yy_brush_money"),
    # 运营修改直评
    path('yy/direct_review_edit/', YyDirectReviewEditView.as_view(), name="yy_direct_review_edit"),
    # 运营修改反馈订单
    path('yy/feedback_record_edit/', YyFeedbackRecordEditView.as_view(), name="yy_edit_feedback_record"),

    # 审核
    path('sh/reset/brush', ShResetBrush.as_view(), name="sh_reset_brush"),
    path('sh/return/check', ShReturnCheckView.as_view(), name="sh_return_check"),
    path('sh/submit/check/', ShSubmitCheckView.as_view(), name="sh_submit_check"),
    path('sh/check/', ShCheckView.as_view(), name="sh_check"),
    path('sh/reset/check/', ShResetCheckView.as_view(), name="sh_reset_check"),
    path('sh/reset/checks/', ShResetChecksView.as_view(), name="sh_reset_checks"),
    path('sh/delete/records/', ShDeleteRecordsView.as_view(), name="sh_delete_records"),
    path('sd/brush/edit/', SdBrushEditView.as_view(), name="sd_brush_edit"),
    # 等待审核页面
    path('sh/check/records/', ShCheckRecordsView.as_view(), name="sh_check_records"),
    # 审核人已审核页面
    path('sh/already/check/records/', ShAlreadyCheckRecordsView.as_view(), name="sh_already_check_records"),
    # 刷单费用查询
    path('sh/brush_money/', ShBrushMoneyView.as_view(), name="sh_brush_money"),
    # 刷单费用总统计
    path('sh/sum_brush_money/', ShSumBrushMoneyView.as_view(), name="sh_sum_brush_money"),
    # 刷单查询
    path('sh/search/records/', ShSearchRecords.as_view(), name="sh_search_records"),
    # 刷单等待提交
    path('sd/brush/records/', SdBrushRecordsView.as_view(), name="sd_brush_records"),
    # 刷单已提交
    path('sd/already/check/records/', SdAlreadyCheckRecords.as_view(), name="sd_already_check_records"),
    # 订单
    path('sdgs/brush/records/', SdgsBrushRecordsView.as_view(), name="sdgs_brush_records"),

    # 刷单
    # 刷单页面
    path('sd/submit/brush/', SdSubmitBrushView.as_view(), name="sd_submit_brush"),
    path('sd/reset/check', SdResetCheck.as_view(), name="sd_reset_check"),
    path('sd/reset/checks', SdResetChecks.as_view(), name="sd_reset_checks"),
    path('sd/search/records', SdSearchRecords.as_view(), name="sd_search_records"),

    # 刷单公司
    # 刷单页面
    path('sdgs/brush/edit/', SdgsBrushEdit.as_view(), name="sdgs_brush_edit"),
    path('sh_sdgs/brush/edit/', ShSdgsBrushEdit.as_view(), name="sh_sdgs_brush_edit"),
    path('sdgs/403/', Sdgs403View.as_view(), name="sdgs_403"),
]
