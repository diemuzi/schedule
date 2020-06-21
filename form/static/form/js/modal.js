/**
 * Search
 */
$(function () {
    let search = $('#search');

    // Delete Modal
    search.on('click', '.btn-delete', function () {
        let url = $(this).attr('data-url');

        $('#delete_modal').modal('show');

        $('#modal_url_delete').attr('action', url);
    });
});