/**
 * Created by AleksZ on 06.01.2017.
 */
/*
 var objs = document.getElementsByClassName("mychart");
 for (var key = 0; key < 199; key++) {
 var name = objs[key].dataset.name;
 var url = objs[key].dataset.url;
 var obj = objs[key]
 var id_num = objs[key].dataset.id;
 getChart(obj, url);
 }
 */
var tooltip = d3.select("body").append("div")
    .attr("class", "my-tooltip")
    .style("opacity", 1)
    .style("position", "absolute")
    .style("z-index","100")
    .style("background", "black")
    .style("color","white")
    .style("padding:", "4px")
    .style("border-radius", "3px");

var canvass = d3.select("body").selectAll("canvas");
canvass.each(function (p, j) {
    var canvas = d3.select(this);
    var url = canvas.attr('data-url');
    getChart(canvas, url);
})
    /*.on('mousemove', function () {
        var canvas = d3.select(this);
        var url = canvas.attr('data-url');
        //var context = canvas.node().getContext("2d");
        var point = d3.mouse(document.body);
        // var x = canvas.pageX;
        //var num_data = canvas.attr('data-id');
        getMouse(canvas, url, point);
    })
    .on("mouseover", function () {
        tooltip.style("display", "inline");
    })
    .on("mouseout", function () {
        tooltip.style("display", "none");
    })*/;

function getChart(canvas, url, id_num) {
    //var canvas = document.querySelector("canvas");
    //context = canvas.getContext("2d");
    //var canvas = d3.select(obj).append("canvas")
    //    .attr("id", "canvas")
    //   .attr("width", 700)
    //   .attr("height", 30);

    var context = canvas.node().getContext("2d");

    //var margin = {top: 20, right: 20, bottom: 30, left: 50},
    //   width = canvas.width - margin.left - margin.right,
    //    height = canvas.height - margin.top - margin.bottom;

    var parseTime = d3.timeParse("%d-%b-%y");
    var parseTime_json = d3.timeParse("%H:%M");

    var x = d3.scaleTime()
        .range([0, 700]);

    var y = d3.scaleLinear()
        .range([30, 0]);

    var line = d3.line()
        .x(function (d) {
            return x(d.x);
        })
        .y(function (d) {
            return y(d.y);
        })
        .curve(d3.curveStep)
        .context(context);

    //context.translate(margin.left, margin.top);
    //var data;

    d3.json(url, function (error, json) {
        if (error) return console.warn(error);
        //data = json;

        y.domain(d3.extent(json, function (d) {
            //d.close = d.close;
            return d.y;
        }));

        x.domain(d3.extent(json, function (d) {
            d.x = parseTime_json(d.x);
            return d.x;
        }));

        context.beginPath();
        line(json);
        context.lineWidth = 1.5;
        context.strokeStyle = "steelblue";
        context.stroke();
    });

    bisectDate = d3.bisector(function (d) {
        return d.x;
    }).left;

    // <div class="chartjs-tooltip" id="tooltip-0"></div>
    // Define the div for the tooltip

};

function getMouse(canvas, url, point) {
    //var canvas = document.querySelector("canvas");
    //context = canvas.getContext("2d");
    //var canvas = d3.select(obj).append("canvas")
    //    .attr("id", "canvas")
    //   .attr("width", 700)
    //   .attr("height", 30);

    var context = canvas.node().getContext("2d");

    //var margin = {top: 20, right: 20, bottom: 30, left: 50},
    //   width = canvas.width - margin.left - margin.right,
    //    height = canvas.height - margin.top - margin.bottom;

    var parseTime = d3.timeParse("%d-%b-%y");
    var parseTime_json = d3.timeParse("%H:%M");

    var x = d3.scaleTime()
        .range([0, 700]);

    var y = d3.scaleLinear()
        .range([30, 0]);

    var line = d3.line()
        .x(function (d) {
            return x(d.x);
        })
        .y(function (d) {
            return y(d.close);
        })
        .curve(d3.curveStep)
        .context(context);

    //context.translate(margin.left, margin.top);
    //var data;

    d3.json(url, function (error, json) {
        if (error) return console.warn(error);
        //data = json;

        y.domain(d3.extent(json, function (d) {
            //d.close = d.close;
            return d.y;
        }));

        x.domain(d3.extent(json, function (d) {
            d.x = parseTime_json(d.x);
            return d.x;
        }));

        //context.beginPath();
        //line(json);
        //context.lineWidth = 1.5;
        //context.strokeStyle = "steelblue";
        //context.stroke();
        var x0 = x.invert(point[0]),
            i = bisectDate(data, x0, 1),
            y0 = data[i].y;
        tooltip.text(x0.getHours() + ':' + x0.getMinutes() + '  speed: ' + y0)
            .style("left", (point[0]+0) + "px")
            .style("top", (point[1]+0) + "px")
            .style("display", "inline");
    });

    bisectDate = d3.bisector(function (d) {
        return d.x;
    }).left;

    // <div class="chartjs-tooltip" id="tooltip-0"></div>
    // Define the div for the tooltip

};


//var div = d3.select('tooltip-0')//.append("div") getElementById('table-chartjs')
//    .attr("id", id_num)
//    .at