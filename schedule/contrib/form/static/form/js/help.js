$(function () {
    $.fn.help_text = function (help_text) {

        let form = $('#form');

        let help_array = form.find('.help-text');

        help_array.each(function () {
            if (help_text === 'True') {
                $(this).show();
            } else {
                $(this).hide();
            }
        });
    };
});