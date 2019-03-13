
const goal_num = 48
function get_data(page,count){
$.ajax({
      type: "POST",
      url: "http://127.0.0.1:8080/get_data",
      data: {
          page: page,
          count: count,
      }
  }).done(function (data) {
      console.log('get returned data');
      console.log(data);
      let obj_data = JSON.parse(data)
      // console.log(type(data));
      // console.log(data_return.name);
      let messageDiv = document.getElementById("value");
      messageDiv.innerHTML += obj_data.breath + '<br>' + obj_data.label + '<br>' + obj_data.timestamp;
      console.log(obj_data.breath);
  });
}

function get_page(page){
$.ajax({
      type: "POST",
      url: "http://127.0.0.1:8080/get_user_page",
      data: {
          page: page,
      }
  }).done(function (data) {
      console.log('get returned data');
      let messageDiv = document.getElementById("value");
      let obj_data = JSON.parse(data);
      console.log(obj_data);
      console.log(typeof(obj_data));
      handle_page_content(obj_data);
      let messageButton = document.getElementsByClassName('button_1')[0];
      console.log(messageButton);
      // messageButton.innerHTML= "<button class='btn btn-info' type='button' data-toggle='collapse' data-target='.multi-collapse' aria-expanded='false' aria-controls='datavis0'>Show breath pattern</button>"
      messageButton.innerHTML= "<button class='btn btn-info' type='button' data-toggle='collapse' data-target='.multi-collapse' aria-expanded='ture' aria-controls='box1 box2'>Show breath pattern</button>"

      // $('.collapse multi-collapse').collapse()
    $('.collapse').collapse()
    // $('.collapse').collapse('show');
    console.log('end')
  });
}

function handle_page_content(data){
    let record_sum = Object.keys(data).length -1;
    console.log(record_sum)
    let messageDiv = document.getElementById("sum");
    messageDiv.innerHTML = '<title>' + 'Completed SMI' + '</title>';
    // messageDiv.innerHTML = '<title>' + 'Completed SMI' + '</title>' + '<p>' + record_sum + '</p>';
    let messageProgress = document.getElementById("progressbar");
    var progress = record_sum/goal_num *100
    messageProgress.innerHTML = "<div class='progress-bar bg-info' role='progressbar' style='width: "+progress+"%;' aria-valuenow='25' aria-valuemin='0' aria-valuemax='100'>"+record_sum+"</div>"
    let record_timestamp = new Array()
    let record_readings = new Array()
    let record_label = new Array()
    for (let i=1;i<=record_sum;i++){
        let per_breath = data[i]
        record_readings[i-1]=per_breath.breath
        record_timestamp[i-1]=per_breath.timestamp
        record_label[i-1] = per_breath.label
    }
    console.log(record_timestamp)
    console.log(record_readings)
    console.log(record_label)
    list_record(record_timestamp,record_readings,record_label)

}

function list_record(record_timestamp,record_readings,record_label){
    let len = record_timestamp.length
    console.log(len)
    let timestamp_str = new Array()
    let messageDivTable = document.getElementsByClassName("table")[0];
    for(let i=0;i<len;i++){
        console.log(record_timestamp[i]);
        let time_num = record_timestamp[i]*1000;
        let date = new Date(time_num);
        timestamp_str[i] = date.toLocaleString(('en'));
    }
    let max_volume = new Array()
    for(let i=0;i<len;i++){
        max_volume[i]=Math.max(...record_readings[i])
    }
    let quality = new Array()
    for(let i=0;i<len;i++){
        if(record_label[i]==1){
            quality[i]='y'
        }
        else{
            quality[i]='x'
        }
    }
    console.log(timestamp_str);
    for(let i=0;i<len;i++){
        let class_name = 'datavis'+i;
        console.log(class_name);
        let class_name_c = '#datavis'+i;
        let box_name ='box'+i;
        messageDivTable.innerHTML += "<tbody>"+
                    "<tr>"+
                      "<th scope='row'>"+i+"</th>"+
                      "<td>"+ timestamp_str[i] +"</td>"+
                      "<td>"+max_volume[i]+"</td>"+
                      "<td>"+quality[i]+"</td>"+
                    "</tr>"+ "</tbody>"
        +"<tbody>"+ "<tr>"+"<div class='collapse multi-collapse' id="+ box_name + ">" + "<div id="+ class_name +"></div>"+"</div>"+
                    "</tr>"+"</tbody>";
        let maxY = max_volume[i]
        let data = record_readings[i]
        draw_data(data,maxY,class_name_c);
    }
    console.log('done')

}

function get_sum(page){
$.ajax({
      type: "POST",
      url: "http://127.0.0.1:8080/get_sum",
      data: {
          page: page,
      }
  }).done(function (data) {
      console.log('get sum');
      let obj_data = JSON.parse(data);
      console.log(obj_data);
  });
}

function draw_data(data,maxY,div_class){
var getdata = -1
var margin = {top: 100, right: 100, bottom: 100, left: 100}
  // , width = window.innerWidth - margin.left - margin.right
width = 400;// Use the window's width
  // , height = window.innerHeight - margin.top - margin.bottom;
height = 200;// Use the window's height
// The number of datapoints
var n = 27;

// 5. X scale will use the index of our data
var xScale = d3.scaleLinear()
    .domain([0, n-1]) // input
    .range([0, width]); // output

// 6. Y scale will use the randomly generate number
var yScale = d3.scaleLinear()
    .domain([0, maxY]) // input
    .range([height, 0]); // output

// 7. d3's line generator
var line = d3.line()
    .x(function(d, i) { return xScale(i); }) // set the x values for the line generator
    .y(function(d) { return yScale(d.y); }) // set the y values for the line generator
    .curve(d3.curveMonotoneX) // apply smoothing to the line

var dataset = d3.range(n).map(function(d) { getdata++; return {"y": data[getdata]}; })
// 1. Add the SVG to the page and employ #2
var svg = d3.select(div_class).append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    // .attr("width", width + 10)
    // .attr("height", height + 10)
  .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

// 3. Call the x axis in a group tag
svg.append("g")
    .attr("class", "x axis")
    .attr("transform", "translate(0," + height + ")")
    .call(d3.axisBottom(xScale)); // Create an axis component with d3.axisBottom

// 4. Call the y axis in a group tag
svg.append("g")
    .attr("class", "y axis")
    .call(d3.axisLeft(yScale)); // Create an axis component with d3.axisLeft

// 9. Append the path, bind the data, and call the line generator
svg.append("path")
    .datum(dataset) // 10. Binds data to the line
    .attr("class", "line") // Assign a class for styling
    .attr("d", line); // 11. Calls the line generator

// 12. Appends a circle for each datapoint
svg.selectAll(".dot")
    .data(dataset)
  .enter().append("circle") // Uses the enter().append() method
    .attr("class", "dot") // Assign a class for styling
    .attr("cx", function(d, i) { return xScale(i) })
    .attr("cy", function(d) { return yScale(d.y) })
    .attr("r", 6)
      .on("mouseover", function(a, b, c) {
  			console.log(a)
        this.attr('class', 'focus')
		})
      .on("mouseout", function() {  })
}




get_page('page_user')
