/**
 * Form Password Meter
 */
$(function () {
    "use strict";

    let password = $('#id_password, #id_password1, #id_new_password1');

    let options = {
        common: {
            minChar: 5,
            debug: false
        },
        rules: {
            raisePower: 1.4
        },
        ui: {
            container: '#pwd-container',
            showStatus: true,
            showProgressBar: false,
            viewports: {
                verdict: '.pwstrength_viewport_verdict'
            }
        }
    };

    password.pwstrength(options);
});