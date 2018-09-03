let counter = 0;
function createData(name, contents) {
  counter += 1;
  return { id: counter, name, contents };
}

var lists = ["Calories", "Fat (g)", "Carbs (g)", "Protein (g)"];
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
    id: "content" + (i + 1),
    numeric: true,
    disablePadding: false,
    label: lists[i]
  });
}

export const recordData = [
  createData("Cupcake", [305, 3.7, 67, 4.3]),
  createData("Donut", [452, 25.0, 51, 4.9]),
  createData("Eclair", [262, 16.0, 24, 6.0]),
  createData("Frozen yoghurt", [159, 6.0, 24, 4.0]),
  createData("Gingerbread", [356, 16.0, 49, 3.9]),
  createData("Honeycomb", [408, 3.2, 87, 6.5]),
  createData("Ice cream sandwich", [237, 9.0, 37, 4.3]),
  createData("Jelly Bean", [375, 0.0, 94, 0.0]),
  createData("KitKat", [518, 26.0, 65, 7.0]),
  createData("Lollipop", [392, 0.2, 98, 0.0]),
  createData("Marshmallow", [318, 0, 81, 2.0]),
  createData("Nougat", [360, 19.0, 9, 37.0]),
  createData("Oreo", [437, 18.0, 63, 4.0])
];