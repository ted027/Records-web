import React from "react";
import PropTypes from "prop-types";
import { withStyles } from "@material-ui/core/styles";
import Table from "@material-ui/core/Table";
import TableBody from "@material-ui/core/TableBody";
import TableCell from "@material-ui/core/TableCell";
import TableHead from "@material-ui/core/TableHead";
import TableRow from "@material-ui/core/TableRow";
import TableSortLabel from "@material-ui/core/TableSortLabel";
import Paper from "@material-ui/core/Paper";
import { hrows, prows, crecordData, cprecordData, precordData, pprecordData, defaultAscListH, defaultAscListP } from "./Records";
import AppBar from '@material-ui/core/AppBar';
import Tabs from '@material-ui/core/Tabs';
import Tab from '@material-ui/core/Tab';
import yellow from '@material-ui/core/colors/yellow';

const styles = theme => ({
  root: {
    width: "100%",
    marginTop: theme.spacing.unit * 3
  },
  table: {
    minWidth: 1020
  },
  tableWrapper: {
    overflowX: "auto"
  },
  tab: {
    flexGrow: 1,
    backgroundColor: theme.palette.background.paper,
  },
});

const CustomTableCellOrder = withStyles(theme => ({
  head: {
    backgroundColor: theme.palette.common.black,
    color: theme.palette.common.white,
    minWidth: 20,
    maxWidth: 20,
    zindex: 3
  },
  body: {
    backgroundColor: theme.palette.common.white,
    fontSize: 14,
    position: "-webkit-sticky",
    position: "sticky",
    left: 0,
    zindex: 1
  }
}))(TableCell);

const CustomTableCellName = withStyles(theme => ({
  head: {
    backgroundColor: theme.palette.common.black,
    color: theme.palette.common.white,
    minWidth: 90,
    zindex: 3,
  },
  body: {
    backgroundColor: theme.palette.common.white,
    fontSize: 14,
    position: "-webkit-sticky",
    position: "sticky",
    minWidth: 90,
    left: 44,
    zindex: 1
  }
}))(TableCell);

const CustomTableCellShort = withStyles(theme => ({
  head: {
    backgroundColor: theme.palette.common.black,
    color: theme.palette.common.white,
    minWidth: 24,
    zindex: 2
  },
  body: {
    fontSize: 14,
    zindex: 0
  }
}))(TableCell);

const CustomTableCell = withStyles(theme => ({
  head: {
    backgroundColor: theme.palette.common.black,
    color: theme.palette.common.white,
    minWidth: 90,
    zindex: 2
  },
  body: {
    fontSize: 14,
    minWidth: 90,
    zindex: 0
  }
}))(TableCell);

const CustomTableSortLabel = withStyles({
  root: {
    "&:hover": {
      color: yellow[600]
    },
    "&:focus": {
      color: yellow[600]
    },
    zindex: 2,
  }
})(TableSortLabel);

function stableSort(array, cmp) {
  const stabilizedThis = array.map((el, index) => [el, index]);
  stabilizedThis.sort((a, b) => {
    const order = cmp(a[0], b[0]);
    if (order !== 0) return order;
    return a[1] - b[1];
  });
  return stabilizedThis.map(el => el[0]);
}

function getSorting(order, orderBy) {
  return order === "asc"
    ? (a, b) => a[orderBy] - b[orderBy]
    : (a, b) => b[orderBy] - a[orderBy];
}

class EnhancedTableHead extends React.Component {

  createSortHandler = property => event => {
    this.props.onRequestSort(event, property);
  };

  render() {
    const { order, orderBy, rows } = this.props;

    return (
      <TableHead>
        <TableRow>
          {rows.map(row => {
            if (row.id === "team") {
              return (
                <CustomTableCellShort
                  key={row.id}
                  numeric={row.numeric}
                  padding={row.disablePadding ? "checkbox" : "none"}
                >
                  {row.label}
                </CustomTableCellShort>
              );
            } else if (row.id === "order") {
              return (
                <CustomTableCellOrder
                  key={row.id}
                  numeric={row.numeric}
                  padding={row.disablePadding ? "checkbox" : "none"}
                >
                  {row.label}
                </CustomTableCellOrder>
              );
            } else if (row.id === "name") {
              return (
                <CustomTableCellName
                  key={row.id}
                  numeric={row.numeric}
                  padding={row.disablePadding ? "checkbox" : "none"}
                >
                  {row.label}
                </CustomTableCellName>
              );
            } else {
              return (
                <CustomTableCell
                  key={row.id}
                  numeric={row.numeric}
                  padding={row.disablePadding ? "checkbox" : "none"}
                  sortDirection={orderBy === row.id ? order : false}
                >
                  <CustomTableSortLabel
                    onClick={this.createSortHandler(row.id)}
                  >
                    {row.label}
                  </CustomTableSortLabel>
                </CustomTableCell>
              );
            }
          }, this)}
          <CustomTableCellShort
            component="th"
            scope="row"
            padding="checkbox"
          />
        </TableRow>
      </TableHead>
    );
  }
}

EnhancedTableHead.propTypes = {
  onRequestSort: PropTypes.func.isRequired,
  order: PropTypes.string.isRequired,
  orderBy: PropTypes.string.isRequired,
  rowCount: PropTypes.number.isRequired,
  rows: PropTypes.array.isRequired,
};

class EnhancedTable extends React.Component {

  state = {
    order: "desc",
    orderBy: "content0",
    orderMean: "good",
    rows: hrows,
    data: crecordData,
    selected: 0,
  };

  handleLeagueChange = (event, selected) => {
    var data;
    var rows;
    var order;
    var orderBy;
    var orderMean;

    if (selected === 0) {
      data = crecordData;
      rows = hrows;
      order = "desc";
    } else if (selected === 1) {
      data = cprecordData;
      rows = prows;
      order = "asc";
    } else if (selected === 2) {
      data = precordData;
      rows = hrows;
      order = "desc";
    } else if (selected === 3) {
      data = pprecordData;
      rows = prows;
      order = "asc";
    }
    orderBy = "content0";
    orderMean = "good";

    this.setState({ selected, data, rows, order, orderBy, orderMean });
  };

  handleRequestSort = (event, property) => {
    const orderBy = property;
    var firstOrder;
    var reverseOrder;
    if ((this.state.selected % 2 && defaultAscListP.indexOf(property) >= 0) ||
       (this.state.selected % 2 === 0 && defaultAscListH.indexOf(property) >= 0)) {
      firstOrder = "asc";
      reverseOrder = "desc";
    } else {
      firstOrder = "desc";
      reverseOrder = "asc";
    }
    let order = firstOrder;
    let orderMean = "good";

    if (this.state.orderBy === property && this.state.order === firstOrder) {
      order = reverseOrder;
      orderMean = "bad";
    }

    this.setState({ order, orderBy, orderMean });
  };

  render() {
    const { classes } = this.props;
    const { data, order, orderBy, selected, rows, orderMean } = this.state;
    var jun;
    var add;
    if (orderMean === "bad") {
      jun = data.length + 1;
      add = -1;
    } else {
      jun = 0;
      add = 1;
    }
    return (
      <Paper className={classes.root}>
        <div className={classes.tab}>
          <AppBar position="static">
            <Tabs
              selected={selected}
              scrollable
              scrollButtons="auto"
              onChange={this.handleLeagueChange}
            >
              <Tab label="CENTRAL HITTERS" />
              <Tab label="CENTRAL PITCHERS" />
              <Tab label="PACIFIC HITTERS" />
              <Tab label="PACIFIC PITCHERS" />
            </Tabs>
          </AppBar>
        </div>
        <div className={classes.tableWrapper}>
          <Table className={classes.table} aria-labelledby="tableTitle">
            <EnhancedTableHead
              order={order}
              orderBy={orderBy}
              onRequestSort={this.handleRequestSort}
              rowCount={data.length}
              rows={rows}
            />
            <TableBody>
              {stableSort(data, getSorting(order, orderBy)).map(n => {
                return (
                  <TableRow hover tabIndex={-1} key={n.id}>
                    <CustomTableCellOrder numeric padding="checkbox">
                      {jun = jun + add}
                    </CustomTableCellOrder>
                    <CustomTableCellName
                      component="th"
                      scope="row"
                      padding="none"
                    >
                      {n.name}
                    </CustomTableCellName>
                    <CustomTableCellShort
                      component="th"
                      scope="row"
                      padding="checkbox"
                    >
                      {n.team}
                    </CustomTableCellShort>
                    <CustomTableCell numeric padding="none">
                      {n.content0}
                    </CustomTableCell>
                    <CustomTableCell numeric padding="none">
                      {n.content1}
                    </CustomTableCell>
                    <CustomTableCell numeric padding="none">
                      {n.content2}
                    </CustomTableCell>
                    <CustomTableCell numeric padding="none">
                      {n.content3}
                    </CustomTableCell>
                    <CustomTableCell numeric padding="none">
                      {n.content4}
                    </CustomTableCell>
                    <CustomTableCell numeric padding="none">
                      {n.content5}
                    </CustomTableCell>
                    <CustomTableCell numeric padding="none">
                      {n.content6}
                    </CustomTableCell>
                    <CustomTableCell numeric padding="none">
                      {n.content7}
                    </CustomTableCell>
                    <CustomTableCell numeric padding="none">
                      {n.content8}
                    </CustomTableCell>
                    <CustomTableCell numeric padding="none">
                      {n.content9}
                    </CustomTableCell>
                    <CustomTableCell numeric padding="none">
                      {n.content10}
                    </CustomTableCell>
                    <CustomTableCell numeric padding="none">
                      {n.content11}
                    </CustomTableCell>
                    <CustomTableCell numeric padding="none">
                      {n.content12}
                    </CustomTableCell>
                    <CustomTableCell numeric padding="none">
                      {n.content13}
                    </CustomTableCell>
                    <CustomTableCell numeric padding="none">
                      {n.content14}
                    </CustomTableCell>
                    <CustomTableCell numeric padding="none">
                      {n.content15}
                    </CustomTableCell>
                    <CustomTableCell numeric padding="none">
                      {n.content16}
                    </CustomTableCell>
                    <CustomTableCell numeric padding="none">
                      {n.content17}
                    </CustomTableCell>
                    <CustomTableCell numeric padding="none">
                      {n.content18}
                    </CustomTableCell>
                    <CustomTableCell numeric padding="none">
                      {n.content19}
                    </CustomTableCell>
                    <CustomTableCell numeric padding="none">
                      {n.content20}
                    </CustomTableCell>
                    <CustomTableCell numeric padding="none">
                      {n.content21}
                    </CustomTableCell>
                    <CustomTableCell numeric padding="none">
                      {n.content22}
                    </CustomTableCell>
                    <CustomTableCell numeric padding="none">
                      {n.content23}
                    </CustomTableCell>
                    <CustomTableCell numeric padding="none">
                      {n.content24}
                    </CustomTableCell>
                    <CustomTableCell numeric padding="none">
                      {n.content25}
                    </CustomTableCell>
                    <CustomTableCell numeric padding="none">
                      {n.content26}
                    </CustomTableCell>
                    <CustomTableCell numeric padding="none">
                      {n.content27}
                    </CustomTableCell>
                    <CustomTableCell numeric padding="none">
                      {n.content28}
                    </CustomTableCell>
                    <CustomTableCell numeric padding="none">
                      {n.content29}
                    </CustomTableCell>
                    <CustomTableCell numeric padding="none">
                      {n.content30}
                    </CustomTableCell>
                    <CustomTableCell numeric padding="none">
                      {n.content31}
                    </CustomTableCell>
                    <CustomTableCell numeric padding="none">
                      {n.content32}
                    </CustomTableCell>
                    <CustomTableCell numeric padding="none">
                      {n.content33}
                    </CustomTableCell>
                    <CustomTableCell numeric padding="none">
                      {n.content34}
                    </CustomTableCell>
                    <CustomTableCell numeric padding="none">
                      {n.content35}
                    </CustomTableCell>
                    <CustomTableCell numeric padding="none">
                      {n.content36}
                    </CustomTableCell>
                    <CustomTableCell numeric padding="none">
                      {n.content37}
                    </CustomTableCell>
                    <CustomTableCell numeric padding="none">
                      {n.content38}
                    </CustomTableCell>
                    <CustomTableCell numeric padding="none">
                      {n.content39}
                    </CustomTableCell>
                    <CustomTableCell numeric padding="none">
                      {n.content40}
                    </CustomTableCell>
                    {selected % 2 === 0 && (
                    <CustomTableCell numeric padding="none">
                      {n.content41}
                    </CustomTableCell>)}
                    {selected % 2 === 0 && (
                    <CustomTableCell numeric padding="none">
                      {n.content42}
                    </CustomTableCell>)}
                    {selected % 2 === 0 && (
                      <CustomTableCell numeric padding="none">
                        {n.content43}
                      </CustomTableCell>)}
                    {selected % 2 === 0 && (
                      <CustomTableCell numeric padding="none">
                        {n.content44}
                      </CustomTableCell>)}
                    {selected % 2 === 0 && (
                      <CustomTableCell numeric padding="none">
                        {n.content45}
                      </CustomTableCell>)}
                    {selected % 2 === 0 && (
                      <CustomTableCell numeric padding="none">
                        {n.content46}
                      </CustomTableCell>)}
                    {selected % 2 === 0 && (
                      <CustomTableCell numeric padding="none">
                        {n.content47}
                      </CustomTableCell>)}
                    {selected % 2 === 0 && (
                      <CustomTableCell numeric padding="none">
                        {n.content48}
                      </CustomTableCell>)}
                    {selected % 2 === 0 && (
                      <CustomTableCell numeric padding="none">
                        {n.content49}
                      </CustomTableCell>)}
                    <CustomTableCellShort
                      component="th"
                      scope="row"
                      padding="checkbox"
                    />
                  </TableRow>
                );
              })}
            </TableBody>
          </Table>
        </div>
      </Paper>
    );
  }
}

EnhancedTable.propTypes = {
  classes: PropTypes.object.isRequired
};

export default withStyles(styles)(EnhancedTable);
