/**
 * Created by AleksZ on 06.01.2017.
 */
function getJSON(url) {
    var resp;
    var xmlHttp;

    resp = '';
    xmlHttp = new XMLHttpRequest();

    if (xmlHttp != null) {
        xmlHttp.open("GET", url, false);
        xmlHttp.send(null);
        resp = xmlHttp.responseText;
    }
    var event = JSON.parse(resp);
    return event;
}

function loadConfig(labels, data) {
    var config = {
        type: 'line',
        data: {
            labels: labels,
            datasets: [{
                label: "My First dataset",
                backgroundColor: window.chartColors.red,
                borderColor: window.chartColors.red,
                pointRadius: 0,
                data: data,
                fill: false,
            }]
        },
        options: {
            responsive: true,
            title: {
                display: false,
                text: 'Chart.js Line Chart'
            },
            legend: {
                display: false,
            },
            tooltips: {
                enabled: false,
                mode: 'index',
                intersect: false,
                custom: customTooltips
            },
            hover: {
                mode: 'nearest',
                intersect: false
            },
            scales: {
                xAxes: [{
                    display: false,
                    scaleLabel: {
                        display: true,
                        labelString: 'Month'
                    }
                }],
                yAxes: [{
                    display: false,
                    scaleLabel: {
                        display: true,
                        labelString: 'Value'
                    }
                }]
            }
        }
    };

    return config
}

var X, Y;
$(document).mousemove(function(e){
    X = e.pageX; // положения по оси X
    Y = e.pageY; // положения по оси Y
    console.log("X: " + X + " Y: " + Y); // вывод результата в консоль
});

var customTooltips = function (tooltip) {
    $(this._chart.canvas).css("cursor", "pointer");

    $(".chartjs-tooltip").css({
        opacity: 0,
    });

    if (!tooltip || !tooltip.opacity) {
        return;
    }

    if (tooltip.dataPoints.length > 0) {
        tooltip.dataPoints.forEach(function (dataPoint) {
            var content = [dataPoint.xLabel, dataPoint.yLabel].join(": ");
            var $tooltip = $("#tooltip-" + dataPoint.datasetIndex);

            $tooltip.html(content);

            $tooltip.css({
                opacity: 1,
                top: (Y+20) + "px",
                left: (X+50) + "px",
            });
        });
    }
};


window.onload = function () {
    var elem = document.getElementById('table-chartjs');
    var elements = elem.getElementsByTagName('canvas');
    for (var i = 0; i < elements.length; i++) {
        var input = elements[i];
        var ctx = input.getContext("2d");
        var url = input.dataset.url;
        var gjson = getJSON(url);
        window.myLine = new Chart(ctx, loadConfig(gjson.labels, gjson.data));

    }
};
