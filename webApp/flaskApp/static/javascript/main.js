$('#form').validate({
    // Validationルール
    rules: {
        username: {
          required: true, 
        },
    },
    // エラーメッセージ
    messages: {
        username: {
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
 