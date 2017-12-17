$(function () {
    console.log(from);
    var from = $('#from');
    var to = $('#to');
    var func = $('#func');
    var out = $('#output');
    $('#plot').click(function (event) {
        event.preventDefault();
        var x = parseFloat(from.val());
        var end = parseFloat(to.val());
        var dx = (end - x) / 100;
        startAnim(x, end, dx, func.val());
    });

    function startAnim(x, end, dx, func) {
        var array = [];
        var interval = setInterval(function () {
            console.log(array);
            array.push([x, eval(func)]);
            $.plot(out, [{label: func, data: array}]);
            x += dx;
            end -= dx;
            if (end < 0) clearInterval(interval);
        }, 100);
        return interval;
    }
});

