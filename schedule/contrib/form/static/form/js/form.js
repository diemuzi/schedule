/**
 * Ajax Form Validation Handler
 */
$(function () {
    /**
     * Form ID
     */
    let form = $('#form');

    /**
     * Add Class
     */
    form.find(
        'input[type="email"], ' +
        'input[type="number"], ' +
        'input[type="password"], ' +
        'input[type="text"], ' +
        'input[type="url"], ' +
        'select, ' +
        'textarea'
    ).addClass('form-control');

    form.find(
        'input[type="checkbox"]'
    ).addClass('custom-control-input');

    /**
     * Remove Class
     */
    form.find(
        'input[type="button"], ' +
        'input[type="checkbox"], ' +
        'input[type="submit"]'
    ).removeClass('form-control');

    /**
     * Fixes Labels to match Form Input fields
     */
    $('label').each(function () {
        let label = $(this);

        // Remove : from all labels (django forms induced)
        label.text(label.text().trim().replace(/:/i, ''));

        let placeholder = label.text();

        label.addClass('font-weight-bold');

        label.closest('.form-group').find('input, textarea').attr('placeholder', placeholder).focus().blur();
    });

    /**
     * Adds CSS for Custom Checkboxes
     */
    $('.custom-checkbox, .custom-switch').each(function () {
        let label = $(this);

        label.find('label').addClass('custom-control-label');
    });

    let submit = $('#submit');

    /**
     * Submit Form
     */
    submit.on('click',
        function () {
            /**
             * Start Block UI
             */
            $.blockUI(
                {
                    message: '<i class="fas fa-spinner fa-pulse fa-5x"></i>',
                    css: {
                        '-webkit-border-radius': '10px',
                        '-moz-border-radius': '10px',
                        backgroundColor: '#000',
                        padding: '15px',
                        border: 'none',
                        opacity: .5,
                        color: '#fff'
                    }
                }
            );

            /**
             * Show Spinner on Submit Button
             */
            submit
                .after('<i class="fas fa-spinner fa-pulse fa-lg" id="busy"></i>')
                .hide();

            /**
             * Get all form fields
             * @type {FormData}
             */
            let form_data = new FormData(form[0]);

            /**
             * Configure
             * @type {*|*|*|*}
             */
            let process = $.ajax(
                {
                    type: 'POST',
                    url: form.attr('action'),
                    dataType: 'json',
                    data: form_data,
                    processData: false,
                    contentType: false,
                    cache: false
                }
            );

            /**
             * Process Form
             */
            process.done(
                function (response) {
                    /**
                     * Form looks good, process and redirect
                     */
                    if (response.success) {
                        window.location = response.redirect;
                    }

                    /**
                     * Create an array of Form Fields
                     */
                    let array = {};

                    for (let key of form_data.keys()) {
                        array[key] = '';
                    }

                    /**
                     * Invalid Fields
                     * Reverse the order so we get the first error
                     */
                    $.each(
                        response, function (key, value) {
                            $.each(
                                value.reverse(), function (message_key, message_value) {
                                    array[key] = message_value;
                                }
                            );
                        }
                    );

                    /**
                     * Remove Icons
                     */
                    $('.form-control-feedback').remove();

                    /**
                     * Filter the array
                     */
                    $.each(
                        array, function (key, value) {
                            let nameKey = $('#id_' + key);

                            let inputKey = $('#input-' + key);

                            if ($('#id_' + key + '-status').is(':visible')) {
                                $('span[id^="id_' + key + '-status"]').remove();
                            }

                            $('label').addClass('form-control-label');

                            /**
                             * Invalid Fields
                             */
                            if (value !== '') {
                                /**
                                 * All Visable Elements Except CSRF
                                 */
                                if (key !== 'csrfmiddlewaretoken' && nameKey.is(':visible')) {
                                    inputKey.find('input, select, textarea')
                                        .removeClass('is-valid')
                                        .addClass('is-invalid');

                                    if (nameKey.is(':checkbox')) {
                                        $('div #input-' + key + ':first label:first').after('<span id="id_' + key + '-status" class="form-text text-danger">' + value + '</span>');
                                    } else {
                                        nameKey.after('<span id="id_' + key + '-status" class="form-text text-danger">' + value + '</span>');
                                    }
                                } else {
                                    /**
                                     * Any hidden errors will be displayed after the submit button
                                     */
                                    submit.after('<span id="id_' + key + '-status" class="form-text text-danger">' + value + '</span>');
                                }
                            }

                            /**
                             * Valid Fields
                             */
                            if (value === '') {
                                /**
                                 * All Element Except CSRF
                                 */
                                if (key !== 'csrfmiddlewaretoken' && nameKey.is(':visible')) {
                                    inputKey.find('input, select, textarea')
                                        .removeClass('is-invalid')
                                        .addClass('is-valid');
                                }
                            }
                        }
                    );
                }
            );

            /**
             * Cleanup once form submission has completed
             */
            process.always(
                function () {
                    /**
                     * End Block UI
                     */
                    $.unblockUI();

                    /**
                     * Show Submit Button
                     */
                    submit.show();

                    /**
                     * Remove Spinner on Submit Button
                     */
                    $('#busy').hide();
                }
            );

            return false;
        }
    );
});