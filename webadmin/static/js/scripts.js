window.onload = function () {
    $('.ajax').on('click', 'input', function () {

            $.ajax({
                url: "/myadmin/sites/link/renew/",

                success: function (data) {
                    $('.ajax_renew').html(data.result);
                    console.log('ajax done');
                },
            });
    });

        $('.ajax3').on('click', 'select', function (event) {

        var target_href = event.target;

        if (target_href) {
            $.ajax({
                url: "/myadmin/sites/detail/view/" + target_href.value + "/",

                success: function (data) {
                    $('.ajax_renew_view').html(data.result);
                    console.log('ajax done');
                },
            });

        }
        event.preventDefault();
    });
}
