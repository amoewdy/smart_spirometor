
function get_data(page,count){
$.ajax({
      type: "POST",
      url: "http://localhost:8080/get_data",
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
      url: "http://localhost:8080/get_user_page",
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
  });
}

function handle_page_content(data){
    let record_sum = Object.keys(data).length -1;
    console.log(record_sum)
    let messageDiv = document.getElementById("sum");
    messageDiv.innerHTML = '<title>' + 'Completed SMI' + '</title>' + '<p>' + record_sum + '</p>';
    let record_timestamp = new Array()
    let record_readings = new Array()
    let record_label = new Array()
    for (let i=1;i<record_sum;i++){
        let per_breath = data[i]
        record_readings[i-1]=per_breath.breath
        record_timestamp[i-1]=per_breath.timestamp
        record_label[i-1] = per_breath.label
    }
    console.log(record_timestamp)
    console.log(record_readings)
    let messageDiv2 = document.getElementById("timeline");
    messageDiv2.innerHTML = '<title>' + 'Time Record' + '</title>'+'</br>'
    messageDiv2.innerHTML += '<p>' + record_timestamp + '</p>'
    draw_time(record_timestamp)

}
function draw_time(record_timestamp){
    let len = record_timestamp.length
    console.log(len)
    for(let i=0;i<len;i++){
        console.log(record_timestamp[i])
        let time_num = record_timestamp[i]*1000
        var date = new Date(time_num)
        console.log(date)
        console.log(date.toLocaleString(('en')));
    }
    // console.log(ts.toString());
}

function get_sum(page){
$.ajax({
      type: "POST",
      url: "http://localhost:8080/get_sum",
      data: {
          page: page,
      }
  }).done(function (data) {
      console.log('get sum');
      let obj_data = JSON.parse(data);
      console.log(obj_data);
  });
}


get_page('page_user')
