/**
 * Search
 */
$(function () {
    let search = $('#search');

    /**
     * DataTable Configuration
     */
    search.DataTable(
        {
            responsive: true,
            render: $.fn.dataTable.render.text(),
            dom: '<<rt> <"row"<"col-md-4 text-left"l> <"col-md-4 text-center"i> <"col-md-4 text-right"p>> >',
        }
    );

    /**
     * DataTable Search Column Inputs
     */
    let search_id = 0;

    $('#search tfoot th').each(function () {
        let title = $(this).text();

        search_id++;

        if ($.trim(title)) {
            $(this).html('<input type="text" placeholder="Search ' + title + '" />');
        } else {
            $(this).html('&nbsp;');
        }
    });

    $('#search tfoot').addClass('d-print-none');

    // DataTable
    let table = search.DataTable();

    // Apply the search
    table.columns().every(function () {
        let that = this;

        $('input', this.footer()).on('keyup change', function () {
            if (that.search() !== this.value) {
                that.search(this.value).draw();
            }
        });
    });

    /**
     * Modals
     */

    // Delete Modal
    search.on('click', '.btn-delete', function (e) {
        let url = $(this).attr('data-url');

        $('#delete_modal').modal('show');

        $('#modal_url_delete').attr('action', url);
    });
});
