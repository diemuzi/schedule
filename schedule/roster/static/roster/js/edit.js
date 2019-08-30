$(function () {
    function convertTime(start_time, end_time) {
        let today = new Date().toLocaleDateString();

        if (start_time.val().length !== 0 && end_time.val().length !== 0) {
            let convert_start = start_time.val().match(/.{1,2}/g);
            let new_start = convert_start.join(":");

            let convert_end = end_time.val().match(/.{1,2}/g);
            let new_end = convert_end.join(":");

            let start_hour = new Date(today + ' ' + new_start + ':00');
            let end_hour = new Date(today + ' ' + new_end + ':00');

            return Math.abs(end_hour - start_hour) / 36e5;
        } else {
            return null;
        }
    }

    function totalTime() {
        let day_array = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday'];
        let total_time = 0;
        let total_time_value = $('#total_time');

        $.each(day_array, function (index, value) {
            let total_day_time = 0;
            let day_is_checked = $('#id_is_' + value).is(':checked');
            let break_is_checked = $('#id_has_break_' + value).is(':checked');
            let day_value = $('#total_' + value);
            let time = convertTime($('input#id_start_time_' + value), $('input#id_end_time_' + value));

            if (time !== null && day_is_checked) {
                total_time += time;
            }

            total_day_time += time;

            if (day_is_checked && break_is_checked) {
                total_time -= .5;
            }

            if (break_is_checked) {
                total_day_time -= .5;
            }

            if (day_is_checked) {
                day_value.closest('p').addClass('text-success');

                day_value.text(total_day_time).addClass('text-dark');
            } else {
                day_value.closest('p').addClass('text-danger');

                day_value.text(total_day_time).addClass('text-dark');
            }
        });

        total_time_value.text(total_time);
    }

    totalTime();
});