window.onload = function () {
    $('.ajax').on('click', 'input', function () {

            $.ajax({
                url: "/myadmin/sites/link/renew/",

                success: function (data) {
                    $('.ajax_new').html(data.result);
                    console.log('ajax done');
                },
            });
    });

    $('.basket_list').on('click', 'input[type="number"]', function (event) {
        var target_href = event.target;

        if (target_href) {
            $.ajax({
                url: "/basket/edit/" + target_href.name + "/" + target_href.value + "/",

                success: function (data) {
                    $('.basket_list').html(data.result);
                    $('.basket_menu').html(data.menu_result);
                    console.log('ajax done');
                },
            });

        }
        event.preventDefault();
    });

}
