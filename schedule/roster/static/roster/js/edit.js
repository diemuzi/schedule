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
            let is_checked = $('#id_is_' + value).is(':checked');
            let day_value = $('#' + value + '_total');
            let time_counter = convertTime($('input#id_' + value + '_start_time_counter'), $('input#id_' + value + '_end_time_counter'));
            let time_outside = convertTime($('input#id_' + value + '_start_time_outside'), $('input#id_' + value + '_end_time_outside'));

            if (time_counter !== null && is_checked) {
                total_time += time_counter
            }

            total_day_time += time_counter;

            if (time_outside !== null && is_checked) {
                total_time += time_outside
            }

            total_day_time += time_outside;

            if (total_day_time > 0) {
                day_value.text(total_day_time);
            } else {
                day_value.text('0');
            }
        });

        total_time_value.text(total_time);
    }

    totalTime();
});