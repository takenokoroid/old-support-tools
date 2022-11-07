jQuery.validator.addMethod(
    "regex",
    function(value, element, regexp) {
        var check = false;
        return this.optional(element) || regexp.test(value);
    }
);
$('#form').validate({
    // Validationルール
    rules: {
        userid: {
          required: true,
          regex : /^[a-zA-Z]{2}[0-9]{4}$/
        },
    },
    // エラーメッセージ
    messages: {
        userid: {
            required: '名前を入力してください',
            regex : '先頭英字2桁+数字4桁で入力してください'
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