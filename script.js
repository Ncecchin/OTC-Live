let act1_title = document.getElementById("act1_title"),
  act1_info = document.getElementById("act1_info"),
  act1_pg = document.getElementById("act1_pg"),
  act2_title = document.getElementById("act2_title"),
  act2_info = document.getElementById("act2_info"),
  act2_pg = document.getElementById("act2_pg"),
  rol1_title = document.getElementById("rol1_title"),
  rol1_info = document.getElementById("rol1_info"),
  rol1_pg = document.getElementById("rol1_pg"),
  rol2_title = document.getElementById("rol2_title"),
  rol2_info = document.getElementById("rol2_info"),
  rol3_title = document.getElementById("rol3_title"),
  rol3_info = document.getElementById("rol3_info"),
  xs63_title = document.getElementById("xs63_title"),
  xs63_info = document.getElementById("xs63_info"),
  xs42_title = document.getElementById("xs42_title"),
  xs42_info = document.getElementById("xs42_info"),
  dia1_title = document.getElementById("dia1_title"),
  dia1_info = document.getElementById("dia1_info"),
  dia2_title = document.getElementById("dia2_title"),
  dia2_info = document.getElementById("dia2_info"),
  dia3_title = document.getElementById("dia3_title"),
  dia3_info = document.getElementById("dia3_info"),
  ths100x_title = document.getElementById("ths100x_title"),
  ths100x_info = document.getElementById("ths100x_info"),
  has1_title = document.getElementById("has1_title"),
  has1_info = document.getElementById("has1_info"),
  has2_title = document.getElementById("has2_title"),
  has2_info = document.getElementById("has2_info"),
  awep_title = document.getElementById("awep_title"),
  awep_info = document.getElementById("awep_info"),
  awe_title = document.getElementById("awe_title"),
  awe_info = document.getElementById("awe_info"),
  tosh1_title = document.getElementById("tosh1_title"),
  tosh1_info = document.getElementById("tosh1_info"),
  tosh2_title = document.getElementById("tosh2_title"),
  tosh2_info = document.getElementById("tosh2_info"),
  tosh3_title = document.getElementById("tosh3_title"),
  tosh3_info = document.getElementById("tosh3_info"),
  ml100_title = document.getElementById("ml100_title"),
  ml100_info = document.getElementById("ml100_info"),
  bf1_title = document.getElementById("bf1_title"),
  bf1_info = document.getElementById("bf1_info"),
  bf2_title = document.getElementById("bf2_title"),
  bf2_info = document.getElementById("bf2_info"),
  bf3_title = document.getElementById("bf3_title"),
  bf3_info = document.getElementById("bf3_info"),
  tarus_title = document.getElementById("tarus_title"),
  tarus_info = document.getElementById("tarus_info"),
  uni_title = document.getElementById("uni_title"),
  uni_info = document.getElementById("uni_info"),
  edm156w_title = document.getElementById("edm156w_title"),
  edm156w_info = document.getElementById("edm156w_info"),
  edmtak_title = document.getElementById("edmtak_title"),
  edmtak_info = document.getElementById("edmtak_info"),
  edmkino85_title = document.getElementById("edmkino85_title"),
  edmkino85_info = document.getElementById("edmkino85_info"),
  rol2_pg = document.getElementById("rol2_pg"),
  rol3_pg = document.getElementById("rol3_pg"),
  xs63_pg = document.getElementById("xs63_pg"),
  xs42_pg = document.getElementById("xs42_pg"),
  dia1_pg = document.getElementById("dia1_pg"),
  dia2_pg = document.getElementById("dia2_pg"),
  dia3_pg = document.getElementById("dia3_pg"),
  ths100x_pg = document.getElementById("ths100x"),
  has1_pg = document.getElementById("has1_pg"),
  has2_pg = document.getElementById("has2_pg"),
  awep_pg = document.getElementById("awep_pg"),
  awe_pg = document.getElementById("awe_pg"),
  tosh1_pg = document.getElementById("tosh1_pg"),
  tosh2_pg = document.getElementById("tosh2_pg"),
  tosh3_pg = document.getElementById("tosh3_pg"),
  ml100_pg = document.getElementById("ml100_pg"),
  bf1_pg = document.getElementById("bf1_pg"),
  bf2_pg = document.getElementById("bf2_pg"),
  bf3_pg = document.getElementById("bf3_pg"),
  tarus_pg = document.getElementById("tarus_pg"),
  uni_pg = document.getElementById("uni_pg"),
  edm156w_pg = document.getElementById("edm156w_pg"),
  edmtak_pg = document.getElementById("edmtak_pg"),
  edmkino85_pg = document.getElementById("edmkino85_pg");

var idList = [
  act1_title,
  act1_info,
  act1_pg,
  act2_title,
  act2_info,
  act1_pg,
  rol1_title,
  rol1_info,
  rol1_pg,
  rol2_title,
  rol2_info,
  rol2_pg,
  rol3_title,
  rol3_info,
  rol3_pg,
  xs63_title,
  xs63_info,
  xs63_pg,
  xs42_title,
  xs42_info,
  xs42_pg,
  dia1_title,
  dia1_info,
  dia1_pg,
  dia2_title,
  dia2_info,
  dia2_pg,
  dia3_title,
  dia3_info,
  dia3_pg,
  ths100x_title,
  ths100x_info,
  ths100x_pg,
  has1_title,
  has1_info,
  has1_pg,
  has2_title,
  has2_info,
  has2_pg,
  awep_title,
  awep_info,
  awep_pg,
  awe_title,
  awe_info,
  awe_pg,
  tosh1_title,
  tosh1_info,
  tosh1_pg,
  tosh2_title,
  tosh2_info,
  tosh2_pg,
  tosh3_title,
  tosh3_info,
  tosh3_pg,
  ml100_title,
  ml100_info,
  ml100_pg,
  bf1_title,
  bf1_info,
  bf1_pg,
  bf2_title,
  bf2_info,
  bf2_pg,
  bf3_title,
  bf3_info,
  bf3_pg,
  tarus_title,
  tarus_info,
  tarus_pg,
  uni_title,
  uni_info,
  uni_pg,
  edm156w_title,
  edm156w_info,
  edm156w_pg,
  edmtak_title,
  edmtak_info,
  edmtak_pg,
  edmkino85_title,
  edmkino85_info,
  edmkino85_pg
];

function valid(x) {
  if (
    x == "-Infinity" ||
    x == "Infinity" ||
    x == "NaN" ||
    x.substring(0, 1) == "-"
  ) {
    return "Unavailable ";
  } else {
    return x;
  }
}

$(document).ready(function() {
  var data = [];
  $.getJSON("/data/liveData/cardData.json", function(result) {
    for (var i = 0; i < result.length; i++) {
      data.push(result[i]);
      var percentage = ((data[i].ptop / data[i].pbot) * 100).toFixed(0);
      idList[i * 3].innerText = data[i].machine;
      idList[i * 3 + 1].innerText =
        data[i].job +
        "\n" +
        data[i].operator +
        "\n" +
        data[i].ipm +
        "\n" +
        data[i].rpm +
        "\n" +
        data[i].file +
        "\n" +
        data[i].procedure +
        "\n" +
        valid(percentage) +
        "%";

      if (data[i].status == 1) {
        idList[i * 3].parentNode.className = "on";
      }

      if (
        data[i].status == -2 ||
        data[i].status == -3 ||
        data[i].status == -4
      ) {
        idList[i * 3].parentNode.className = "uk";
      }

      if (data[i].status == 0) {
        idList[i * 3].parentNode.className = "off";
      }
    }
    console.log(data);
  });
});
