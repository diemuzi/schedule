/**
 * Custom
 */
$(function () {
    /**
     * Prevent link from following its href
     */
    $('a[aria-disabled="true"]').on('click', function (event) {
        event.preventDefault();
    });

    /**
     * Message Timeout
     */
    window.setTimeout(
        function () {
            $('.alert-dismissible')
                .alert('close');
        }, 10000
    );

    /**
     * Always scroll to top on-load
     */
    window.scrollTo(0, 0);
});