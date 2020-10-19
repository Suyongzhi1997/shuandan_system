//顶部搜索栏搜索方法
function search_record() {
    var keywords = $('#search_keywords').val(),
        request_url = '';
    if (keywords == "") {
        return
    }
    url_part = window.location.pathname;
    request_url = url_part + "?keywords=" + keywords;
    window.location.href = request_url;
}


function kf_search_record() {
    var keywords = $('#kf_search_keywords').val(),
        request_url = '';
    if (keywords == "") {
        return
    }
    url_part = window.location.pathname;
    request_url = url_part + "?keywords=" + keywords + '&search_type=' + $("#search-type option:selected").val();
    window.location.href = request_url;
}

function yy_search_info() {
    var keywords = $('#search_keywords').val(),
        request_url = '';
    if (keywords == "") {
        return
    }
    url_part = window.location.pathname;
    request_url = url_part + "?keywords=" + keywords + '&search_type=' + $("#search-type option:selected").val();
    window.location.href = request_url;
}

$("#search_keywords").keydown(function (event) {
    if (event.keyCode == 13) {
        search_record();
    }
});

$("#kf_search_keywords").keydown(function (event) {
    if (event.keyCode == 13) {
        kf_search_record();
    }
});

function edit_form(object) {
    let $currentTrEle = $(object).parent().parent();
    let record_id = $currentTrEle.children().eq(0).find('input').eq(0).attr("value");
    $("#record_id").val(record_id);

    let ASIN = $currentTrEle.children().eq(1).attr("title");
    $("#ASIN").val(ASIN);

    let c_price = $currentTrEle.children().eq(2).attr("title");
    $("#c_price").val(c_price);

    let purchase_cost = $currentTrEle.children().eq(3).attr("title");
    $("#purchase_cost").val(purchase_cost);

    let product_profit = $currentTrEle.children().eq(4).attr("title");
    $("#product_profit").val(product_profit);

    let product_upload_time = $currentTrEle.children().eq(5).attr("title");
    $("#product_upload_time").datepicker('setValue', product_upload_time);

    // let brush_number = $currentTrEle.children().eq(6).attr("title");
    // $("#brush_number").val(brush_number);

    let sale_30_number = $currentTrEle.children().eq(6).attr("title");
    $("#sale_30_number").val(sale_30_number);

    let sale_7_number = $currentTrEle.children().eq(7).attr("title");
    $("#sale_7_number").val(sale_7_number);

    let record_src = $currentTrEle.children().eq(1).find('a').attr("href");
    $("#record_src").val(record_src);

    let feedback = $currentTrEle.children().eq(8).attr("title");
    if (feedback === "1") {
        $("#review_type").val("feedback");
    }

    let review_number = $currentTrEle.children().eq(9).attr("title");
    if (review_number === "1") {
        $("#review_type").val("留评");
    }

    let direct_review = $currentTrEle.children().eq(10).attr("title");
    if (direct_review === "1") {
        $("#review_type").val("直评");
    }

    let free_review_number = $currentTrEle.children().eq(11).attr("title");
    if (free_review_number === "1") {
        $("#review_type").val("免评");
    }

    let now_score = $currentTrEle.children().eq(12).attr("title");
    $("#now_score").val(now_score);

    let now_review_number = $currentTrEle.children().eq(13).attr("title");
    $("#now_review_number").val(now_review_number);

    $('#my-prompt').modal();
}

function username_edit() {
    $('#my-prompt-username').modal();
}

function userpwd_edit() {
    $('#my-prompt-userpwd').modal();
}


$(".edit-record").click(function () {
    let $currentTrEle = $(this).parent().parent();
    let record_id = $currentTrEle.children().eq(0).find('input').attr("value");
    let site = $currentTrEle.children().eq(3).attr("title");
    let shop = $currentTrEle.children().eq(4).attr("title");
    let product_chinese_name = $currentTrEle.children().eq(5).attr("title");
    let SKU = $currentTrEle.children().eq(6).attr("title");
    let order_word = $currentTrEle.children().eq(8).attr("title");
    let order_date = $currentTrEle.children().eq(13).attr("title");
    let review_date = $currentTrEle.children().eq(14).attr("title");
    let key_word_page_number = $currentTrEle.children().eq(15).attr("title");
    let key_word_link = $currentTrEle.children().eq(17).attr("title");
    let c_price = $currentTrEle.children().eq(18).attr("title");

    $("#site").val(site);
    $("#shop").val(shop);
    $("#product_chinese_name").val(product_chinese_name);
    $("#SKU").val(SKU);
    $("#order_word").val(order_word);
    $("#key_word_page_number").val(key_word_page_number);
    $("#key_word_link").val(key_word_link);
    $("#c_price").val(c_price);
    $("#record_id").val(record_id);
    $("#order_date").datepicker('setValue', order_date);
    $("#review_date").datepicker('setValue', review_date);

    $('#my-prompt').modal();
});

$('input[id="selectAll"]').click(function () {
    //alert(this.checked);
    if ($(this).is(':checked')) {
        $('input[name="ids"]').each(function () {
            //此处如果用attr，会出现第三次失效的情况
            $(this).prop("checked", true);
        });
    } else {
        $('input[name="ids"]').each(function () {
            $(this).removeAttr("checked", false);
        });
        //$(this).removeAttr("checked");
    }

});


function download_info_file() {
    var obj = document.getElementsByClassName('record-checkbox'); //选择所有classname="'test'"的对象，返回数组
    //取到对象数组后，我们来循环检测它是不是被选中
    var s = '';
    for (var i = 0; i < obj.length; i++) {
        if (obj[i].checked) s += obj[i].value + '_'; //如果选中，将value添加到变量s中
    }
    //那么现在来检测s的值就知道选中的复选框的值了
    if (s == '') {
        alert('你还没有选择任何内容！');
    } else {
        $.ajax({
            url: "/file/download/info/?id_data=" + s,
            type: "GET",

            // {#请求成功回调函数#}
            success: function (data) {
                window.open('http://127.0.0.1:8000/' + data.file_name);
            },
            // {#请求失败回调函数#}
            error: function () {
                alert("服务器请求超时,请重试!");
            }

        });
    }
}

function download_all_info_file() {
    $.ajax({
        url: "/file/download/all_info/",
        type: "GET",

        // {#请求成功回调函数#}
        success: function (data) {
            window.open('http://127.0.0.1:8000/' + data.file_name);
        },
        // {#请求失败回调函数#}
        error: function () {
            alert("服务器请求超时,请重试!");
        }

    });
}

function download_file() {
    var obj = document.getElementsByClassName('record-checkbox'); //选择所有classname="'test'"的对象，返回数组
    //取到对象数组后，我们来循环检测它是不是被选中
    var s = '';
    for (var i = 0; i < obj.length; i++) {
        if (obj[i].checked) s += obj[i].value + '_'; //如果选中，将value添加到变量s中
    }
    //那么现在来检测s的值就知道选中的复选框的值了
    if (s == '') {
        alert('你还没有选择任何内容！');
    } else {
        $.ajax({
            url: "/file/download/?id_data=" + s,
            type: "GET",

            // {#请求成功回调函数#}
            success: function (data) {
                window.open('http://127.0.0.1:8000/' + data.file_name);
            },
            // {#请求失败回调函数#}
            error: function () {
                alert("服务器请求超时,请重试!");
            }

        });
    }
}


function download_all_file() {
    $.ajax({
            url: "/file/download/all_record/",
            type: "GET",

            // {#请求成功回调函数#}
            success: function (data) {
                window.open('http://127.0.0.1:8000/' + data.file_name);
            },
            // {#请求失败回调函数#}
            error: function () {
                alert("服务器请求超时,请重试!");
            }

        });
}

function sdgs_download_file() {
    var obj = document.getElementsByClassName('record-checkbox'); //选择所有classname="'test'"的对象，返回数组
    //取到对象数组后，我们来循环检测它是不是被选中
    var s = '';
    for (var i = 0; i < obj.length; i++) {
        if (obj[i].checked) s += obj[i].value + '_'; //如果选中，将value添加到变量s中
    }
    //那么现在来检测s的值就知道选中的复选框的值了
    if (s == '') {
        alert('你还没有选择任何内容！');
    } else {
        $.ajax({
            url: "/file/sdgs_download/?id_data=" + s,
            type: "GET",

            // {#请求成功回调函数#}
            success: function (data) {
                if (data.file_name){
                    window.open('http://127.0.0.1:8000/' + data.file_name);
                }else{
                    window.location.href=data.url;
                }

            },
            // {#请求失败回调函数#}
            error: function () {
                alert("服务器请求超时,请重试!");
            }

        });
    }
}

function brush_money_download_file() {
    var obj = document.getElementsByClassName('record-checkbox'); //选择所有classname="'test'"的对象，返回数组
    //取到对象数组后，我们来循环检测它是不是被选中
    var s = '';
    for (var i = 0; i < obj.length; i++) {
        if (obj[i].checked) s += obj[i].value + '_'; //如果选中，将value添加到变量s中
    }
    //那么现在来检测s的值就知道选中的复选框的值了
    if (s == '') {
        alert('你还没有选择任何内容！');
    } else {
        $.ajax({
            url: "/file/download/brush_money/?id_data=" + s,
            type: "GET",

            // {#请求成功回调函数#}
            success: function (data) {
                window.open('http://127.0.0.1:8000/' + data.file_name);
            },
            // {#请求失败回调函数#}
            error: function () {
                alert("服务器请求超时,请重试!");
            }

        });
    }
}


function upload(object) {
    // alert($(object).parent());
    let $currentFormEle = $(object).parent().parent();
    $currentFormEle.submit();
}

function download_template_file(object) {
    let s = object.value;
    if (s === '') {
        alert('你还没有选择任何内容！');
    }
    $.ajax({
        url: "/file/download/template/?filename=" + s,
        type: "GET",

        // {#请求成功回调函数#}
        success: function (data) {
            window.open('http://127.0.0.1:8000/' + data.file_name);
        },
        // {#请求失败回调函数#}
        error: function () {
            alert("服务器请求超时,请重试!");
        }

    });
}

function fb_favorite(object) {
    var obj = document.getElementsByClassName('record-checkbox'); //选择所有classname="'test'"的对象，返回数组
    //取到对象数组后，我们来循环检测它是不是被选中
    var s = '';
    for (var i = 0; i < obj.length; i++) {
        if (obj[i].checked) s += obj[i].value + '_'; //如果选中，将value添加到变量s中
    }
    //那么现在来检测s的值就知道选中的复选框的值了
    if (s == '') {
        alert('你还没有选择任何内容！');
    } else {
        $.ajax({
            url: "/record/favorite/fb/?id_data=" + s + "&next=" + $(object).attr("value"),
            type: "GET",

            // {#请求成功回调函数#}
            success: function (data) {
                window.location.href = data.next_url;
            },
            // {#请求失败回调函数#}
            error: function () {
                alert("服务器请求超时,请重试!");
            }
        });
    }
}

function check_form(object) {
    let $currentTrEle = $(object).parent().parent();
    let record_id = $currentTrEle.children().eq(0).find('input').eq(0).attr("value");
    $("#record_id").val(record_id);

    let audit_results = $currentTrEle.children().eq(16).find('select').val();
    $("#modal_audit_results").val(audit_results);

    let remark = $currentTrEle.children().eq(17).attr("title");
    $("#remark").val(remark);

    $('#my-prompt').modal();
}

function edit_feedback(object) {
    let $currentTrEle = $(object).parent().parent();
    let record_id = $currentTrEle.children().eq(0).find('input').eq(0).attr("value");
    $("#record_id").val(record_id);
    let brush_company = $currentTrEle.children().eq(16).attr("title");

    if (brush_company != '-1') {
        $("#brush_company").val(brush_company);
    }

    let order_number = $currentTrEle.children().eq(17).attr("title");
    $("#order_number").val(order_number);

    let brush_money = $currentTrEle.children().eq(18).attr("title");
    $("#brush_money").val(brush_money);

    let review_feedback = $currentTrEle.children().eq(19).attr("title");
    $("#review_feedback").val(review_feedback);

    let record_status = $currentTrEle.children().eq(20).attr("title");
    $("#record_status").val(record_status);

    $('#my-prompt').modal();
}

function yy_edit_feedback(object) {
    let $currentTrEle = $(object).parent().parent();
    let record_id = $currentTrEle.children().eq(0).find('input').eq(0).attr("value");
    $("#record_id").val(record_id);

    let record_status = $currentTrEle.children().eq(20).attr("title");
    $("#record_status").val(record_status);

    $('#my-prompt').modal();
}

function sh_edit_feedback(object) {
    let $currentTrEle = $(object).parent().parent();
    let record_id = $currentTrEle.children().eq(0).find('input').eq(0).attr("value");
    $("#record_id").val(record_id);

    let order_number = $currentTrEle.children().eq(17).attr("title");
    $("#order_number").val(order_number);

    let brush_money = $currentTrEle.children().eq(18).attr("title");
    $("#brush_money").val(brush_money);

    let review_feedback = $currentTrEle.children().eq(19).attr("title");
    $("#review_feedback").val(review_feedback);

    let record_status = $currentTrEle.children().eq(20).attr("title");
    $("#record_status").val(record_status);

    let record_settlement = $currentTrEle.children().eq(21).attr("title");
    $("#record_settlement").val(record_settlement);

    $('#my-prompt').modal();
}

function sdgs_edit_feedback(object) {
    let $currentTrEle = $(object).parent().parent();
    let record_id = $currentTrEle.children().eq(0).find('input').eq(0).attr("value");
    $("#record_id").val(record_id);

    let order_number = $currentTrEle.children().eq(15).attr("title");
    $("#order_number").val(order_number);

    let brush_money  = $currentTrEle.children().eq(16).attr("title");
    $("#brush_money").val(brush_money);

    let review_feedback = $currentTrEle.children().eq(17).attr("title");
    $("#review_feedback").val(review_feedback);

    let record_status = $currentTrEle.children().eq(18).attr("title");
    $("#record_status").val(record_status);

    $('#my-prompt').modal();
}

function submit_check(object) {
    var obj = document.getElementsByClassName('record-checkbox'); //选择所有classname="'test'"的对象，返回数组
    //取到对象数组后，我们来循环检测它是不是被选中
    var s = '';
    for (var i = 0; i < obj.length; i++) {
        if (obj[i].checked) s += obj[i].value + '_'; //如果选中，将value添加到变量s中
    }
    //那么现在来检测s的值就知道选中的复选框的值了
    if (s == '') {
        alert('你还没有选择任何内容！');
    } else {
        let $currentFormEle = $(object).parent().parent();
        $('#check_ids').val(s);
        $currentFormEle.submit();
    }

}

function submit_delete(object) {
    var obj = document.getElementsByClassName('record-checkbox'); //选择所有classname="'test'"的对象，返回数组
    //取到对象数组后，我们来循环检测它是不是被选中
    var s = '';
    for (var i = 0; i < obj.length; i++) {
        if (obj[i].checked) s += obj[i].value + '_'; //如果选中，将value添加到变量s中
    }
    //那么现在来检测s的值就知道选中的复选框的值了
    if (s == '') {
        alert('你还没有选择任何内容！');
    } else {
        let $currentFormEle = $(object).parent().parent();
        $('#delete_check_ids').val(s);
        $currentFormEle.submit();
    }

}



function sh_submit_check(object) {
    var obj = document.getElementsByClassName('record-checkbox'); //选择所有classname="'test'"的对象，返回数组
    //取到对象数组后，我们来循环检测它是不是被选中
    var s = '';
    let check_result = '';
    for (var i = 0; i < obj.length; i++) {
        if (obj[i].checked) {
            s += obj[i].value + '_';
            let $currentTrEle = $(obj[i]).parent().parent();
            check_result += $currentTrEle.children().eq(16).find('select').val() + '_';
        } //如果选中，将value添加到变量s中
    }
    //那么现在来检测s的值就知道选中的复选框的值了
    if (s == '') {
        alert('你还没有选择任何内容！');
    } else {
        let $currentFormEle = $(object).parent().parent();
        $('#check_ids').val(s);
        $('#check_datas').val(check_result);
        $currentFormEle.submit();
    }

}

function favorite(object) {
    var obj = document.getElementsByClassName('record-checkbox'); //选择所有classname="'test'"的对象，返回数组
    //取到对象数组后，我们来循环检测它是不是被选中
    var s = '';
    for (var i = 0; i < obj.length; i++) {
        if (obj[i].checked) s += obj[i].value + '_'; //如果选中，将value添加到变量s中
    }
    //那么现在来检测s的值就知道选中的复选框的值了
    if (s == '') {
        alert('你还没有选择任何内容！');
    } else {
        $.ajax({
            url: "/record/favorite/?id_data=" + s + "&next=" + $(object).attr("value"),
            type: "GET",

            // {#请求成功回调函数#}
            success: function (data) {
                window.location.href = data.next_url;
            },
            // {#请求失败回调函数#}
            error: function () {
                alert("服务器请求超时,请重试!");
            }
        });
    }
}

function add_info() {
    $("#add-prompt").modal();
}

function edit_promote_info(object) {
    let $currentTrEle = $(object).parent().parent();
    let info_id = $currentTrEle.children().eq(0).find('input').eq(0).attr("value");
    $("#info_id").val(info_id);

    let asin = $currentTrEle.children().eq(2).attr("title");
    $("#asin").val(asin);

    let content = $currentTrEle.children().eq(3).attr("title");
    $("#content").val(content);

    let yy_remark = $currentTrEle.children().eq(4).attr("title");
    $("#yy_remark").val(yy_remark);

    $("#product_form").attr("action","/promote/edit_info/");
    $("#add-prompt").modal();
}

function add_record_info() {
    document.getElementById("add_record_form").reset();
    $("#my-prompt").modal();
    $("#add_record_form").attr("action","/record/yy/add/check/");
}

function edit_info(object) {
    let $currentTrEle = $(object).parent().parent();
    let info_id = $currentTrEle.children().eq(0).find('input').eq(0).attr("value");
    $("#info_id").val(info_id);

    let send_time = $currentTrEle.children().eq(1).attr("title");
    if (send_time !== '') {
        $("#send_time").datepicker('setValue', send_time);
    }
    let send_company = $currentTrEle.children().eq(2).attr("title");
    $("#send_company").val(send_company);

    let channel = $currentTrEle.children().eq(3).attr("title");
    $("#channel").val(channel);

    let site = $currentTrEle.children().eq(4).attr("title");
    $("#site").val(site);

    let country = $currentTrEle.children().eq(6).attr("title");
    $("#country").val(country);

    let track_number = $currentTrEle.children().eq(7).attr("title");
    $("#track_number").val(track_number);

    let net_weight = $currentTrEle.children().eq(8).attr("title");
    $("#net_weight").val(net_weight);

    let volume_weight = $currentTrEle.children().eq(9).attr("title");
    $("#volume_weight").val(volume_weight);

    let actual_charged_weight = $currentTrEle.children().eq(10).attr("title");
    $("#actual_charged_weight").val(actual_charged_weight);

    let pieces_number = $currentTrEle.children().eq(11).attr("title");
    $("#pieces_number").val(pieces_number);

    let includes_price = $currentTrEle.children().eq(12).attr("title");
    $("#includes_price").val(includes_price);

    let other_price = $currentTrEle.children().eq(13).attr("title");
    $("#other_price").val(other_price);

    let total_price = $currentTrEle.children().eq(14).attr("title");
    $("#total_price").val(total_price);

    let express_time = $currentTrEle.children().eq(15).attr("title");
    if (express_time !== '') {
        $("#express_time").datepicker('setValue', express_time);
    }


    let express_status = $currentTrEle.children().eq(16).attr("title");
    $("#express_status").val(express_status);

    let settlement = $currentTrEle.children().eq(17).attr("title");
    $("#settlement").val(settlement);

    let order_remark = $currentTrEle.children().eq(18).attr("title");
    $("#order_remark").val(order_remark);

    $("#my-prompt").modal();
}

function edit_project_info(object) {
    let $currentTrEle = $(object).parent().parent();
    let info_id = $currentTrEle.children().eq(0).find('input').eq(0).attr("value");
    $("#info_id").val(info_id);

    let company = $currentTrEle.children().eq(6).attr("title");
    $("#company").val(company);

    let cost = $currentTrEle.children().eq(7).attr("title");
    $("#cost").val(cost);

    let sh_remark = $currentTrEle.children().eq(8).attr("title");
    $("#sh_remark").val(sh_remark);

    $("#my-prompt").modal();
}

function unfavorite(object) {
    var obj = document.getElementsByClassName('record-checkbox'); //选择所有classname="'test'"的对象，返回数组
    //取到对象数组后，我们来循环检测它是不是被选中
    var s = '';
    for (var i = 0; i < obj.length; i++) {
        if (obj[i].checked) s += obj[i].value + '_'; //如果选中，将value添加到变量s中
    }
    //那么现在来检测s的值就知道选中的复选框的值了
    if (s == '') {
        alert('你还没有选择任何内容！');
    } else {
        $.ajax({
            url: "/record/unfavorite/?id_data=" + s + "&next=" + $(object).attr("value"),
            type: "GET",

            // {#请求成功回调函数#}
            success: function (data) {
                window.location.href = data.next_url;
            },
            // {#请求失败回调函数#}
            error: function () {
                alert("服务器请求超时,请重试!");
            }
        });
    }
}

function unfbfavorite(object) {
    var obj = document.getElementsByClassName('record-checkbox'); //选择所有classname="'test'"的对象，返回数组
    //取到对象数组后，我们来循环检测它是不是被选中
    var s = '';
    for (var i = 0; i < obj.length; i++) {
        if (obj[i].checked) s += obj[i].value + '_'; //如果选中，将value添加到变量s中
    }
    //那么现在来检测s的值就知道选中的复选框的值了
    if (s == '') {
        alert('你还没有选择任何内容！');
    } else {
        $.ajax({
            url: "/record/unfavorite/fb/?id_data=" + s + "&next=" + $(object).attr("value"),
            type: "GET",

            // {#请求成功回调函数#}
            success: function (data) {
                window.location.href = data.next_url;
            },
            // {#请求失败回调函数#}
            error: function () {
                alert("服务器请求超时,请重试!");
            }
        });
    }
}

function delete_delivery(object) {
    var obj = document.getElementsByClassName('record-checkbox'); //选择所有classname="'test'"的对象，返回数组
    //取到对象数组后，我们来循环检测它是不是被选中
    var s = '';
    for (var i = 0; i < obj.length; i++) {
        if (obj[i].checked) s += obj[i].value + '_'; //如果选中，将value添加到变量s中
    }
    //那么现在来检测s的值就知道选中的复选框的值了
    if (s == '') {
        alert('你还没有选择任何内容！');
    } else {
        $.ajax({
            url: "/delivery/delete_info/?id_data=" + s + "&next=" + $(object).attr("value"),
            type: "GET",

            // {#请求成功回调函数#}
            success: function (data) {
                window.location.href = data.next_url;
            },
            // {#请求失败回调函数#}
            error: function () {
                alert("服务器请求超时,请重试!");
            }
        });
    }
}

function edit_direct_review(object) {
    let record_id = $(object).attr("record_id");
    let direct_review_title = $(object).attr("direct_review_title");
    let direct_review_content = $(object).attr("direct_review_content");
    let direct_review_remark = $(object).attr("direct_review_remark");

    if (direct_review_remark !== "None") {
        $("#direct_review_remark").val(direct_review_remark);
    }
    $("#direct_review_record_id").val(record_id);
    $("#direct_review_title").val(direct_review_title);
    $("#direct_review_content").val(direct_review_content);


    $("#direct-review-prompt").modal();
}