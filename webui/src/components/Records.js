import obj from '../records.json';

var records = obj.records;

let counter = 0;
function createData(name, team, contents) {
  counter += 1;
  var content0 = contents[0];
  var content1 = contents[1];
  var content2 = contents[2];
  var content3 = contents[3];
  var content4 = contents[4];
  var content5 = contents[5];
  var content6 = contents[6];
  var content7 = contents[7];
  var content8 = contents[8];
  var content9 = contents[9];
  var content10 = contents[10];
  var content11 = contents[11];
  var content12 = contents[12];
  var content13 = contents[13];
  var content14 = contents[14];
  var content15 = contents[15];
  var content16 = contents[16];
  var content17 = contents[17];
  var content18 = contents[18];
  var content19 = contents[19];
  var content20 = contents[20];
  var content21 = contents[21];
  var content22 = contents[22];
  var content23 = contents[23];
  var content24 = contents[24];
  var content25 = contents[25];
  var content26 = contents[26];
  var content27 = contents[27];
  var content28 = contents[28];
  var content29 = contents[29];
  var content30 = contents[30];
  var content31 = contents[31];
  var content32 = contents[32];
  var content33 = contents[33];
  var content34 = contents[34];
  var content35 = contents[35];
  var content36 = contents[36];
  var content37 = contents[37];
  var content38 = contents[38];
  var content39 = contents[39];
  var content40 = contents[40];
  var content41 = contents[41];
  var content42 = contents[42];
  var content43 = contents[43];
  var content44 = contents[44];
  var content45 = contents[45];
  var content46 = contents[46];
  var content47 = contents[47];
  var content48 = contents[48];
  var content49 = contents[49];
  return {
    id: counter,
    name,
    team,
    content0,
    content1,
    content2,
    content3,
    content4,
    content5,
    content6,
    content7,
    content8,
    content9,
    content10,
    content11,
    content12,
    content13,
    content14,
    content15,
    content16,
    content17,
    content18,
    content19,
    content20,
    content21,
    content22,
    content23,
    content24,
    content25,
    content26,
    content27,
    content28,
    content29,
    content30,
    content31,
    content32,
    content33,
    content34,
    content35,
    content36,
    content37,
    content38,
    content39,
    content40,
    content41,
    content42,
    content43,
    content44,
    content45,
    content46,
    content47,
    content48,
    content49
  };
}
var lists = records[0].slice(2, records[0].length);

export const rows = [
  {
    id: "order",
    numeric: false,
    disablePadding: true
  },
  {
    id: "name",
    numeric: false,
    disablePadding: true,
    label: "氏名"
  },
  {
    id: "team",
    numeric: false,
    disablePadding: true,
    label: "球団"
  }
];

for (var i = 0; i < lists.length; i++) {
  rows.push({
    id: "content" + i,
    numeric: true,
    disablePadding: false,
    label: lists[i]
  });
}

export const recordData = [];
for (var j = 1; j < records.length; j++) {
  recordData.push(
    createData(
      records[j][0],
      records[j][1],
      records[j].slice(2, records[0].length)
    )
  );
}
