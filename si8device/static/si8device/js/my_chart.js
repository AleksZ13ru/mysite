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
                mode: 'index',
                intersect: false,
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
window.onload = function () {
    var elem = document.getElementById('my_chart');
    var elements = elem.getElementsByTagName('canvas');
    for (var i = 0; i < elements.length; i++) {
        var input = elements[i];
        var ctx = input.getContext("2d");
        var url = input.dataset.url;
        var gjson = getJSON(url);
        var labels = gjson.labels;
        var data = gjson.data;
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
                    mode: 'index',
                    intersect: false,
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
        window.myLine = new Chart(ctx, config);
    }
};
