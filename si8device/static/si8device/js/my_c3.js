/**
 * Created by AleksZ on 03.01.2017.
 */
window.onload = function () {
    var objs = document.getElementsByClassName("mychart");
    for (var key = 0; key < 10; key++) {
        var name = objs[key].dataset.name;
        var url = objs[key].dataset.url;
        getChart(name, url);

    }
};

function getChart(name, url) {

    var chart = c3.generate(
        {
            bindto: name,
            size: {
                width: 700,
                height: 30
            },
            legend: {
                show: false
            },
            axis: {
                x: {
                    type: 'category',
                    show: false
                },
                y: {
                    show: false
                }
            },
            point: {
                show: false
            },
            data: {
                x: "date",
                //url: 'http://127.0.0.1:8000/si8/line_chartc3/json/',
                url: url,
                mimeType: 'json'
            }
        });
}
