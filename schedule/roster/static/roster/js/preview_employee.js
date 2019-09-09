$(function () {
    function totalTime() {
        let day_array = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday'];
        let total_time = 0;
        let total_time_value = $('#total_time');

        $.each(day_array, function (index, value) {
            let day_value = parseFloat($('#' + value).text()) || 0;

            if (day_value !== undefined || day_value !== 0) {
                console.log(day_value);

                total_time += day_value;

                console.log(total_time);
            }
        });

        total_time_value.text(total_time);
    }

    totalTime();
});