$('#form').validate({
    // Validationルール
    rules: {
        userid: {
          required: true, 
        },
    },
    // エラーメッセージ
    messages: {
        userid: {
            required: '名前を入力してください',
        },
    },
 
    // エラーメッセージ出力箇所
    errorPlacement: function(error, element){
        var name = element.attr('name');
        error.appendTo($('.is-error-'+name));
    },
 
    errorElement: "span",
    errorClass: "is-error",
});
 
$(function () {
	$('[data-toggle="tooltip"]').tooltip();
});