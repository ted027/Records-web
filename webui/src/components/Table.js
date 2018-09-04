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
import Tooltip from "@material-ui/core/Tooltip";
import { rows, recordData } from "./Records";

function desc(a, b, orderBy) {
  if (b[orderBy] < a[orderBy]) {
    return -1;
  }
  if (b[orderBy] > a[orderBy]) {
    return 1;
  }
  return 0;
}

function getSorting(order, orderBy) {
  return order === "desc"
    ? (a, b) => desc(a, b, orderBy)
    : (a, b) => -desc(a, b, orderBy);
}

class EnhancedTableHead extends React.Component {
  createSortHandler = property => event => {
    this.props.onRequestSort(event, property);
  };

  render() {
    const { order } = this.props;

    return (
      <TableHead>
        <TableRow>
          {rows.map(row => {
            return (
              <TableCell
                key={row.id}
                numeric={row.numeric}
                padding={row.disablePadding ? "none" : "default"}
              >
                <Tooltip
                  title="Sort"
                  placement={row.numeric ? "bottom-end" : "bottom-start"}
                  enterDelay={300}
                >
                  <TableSortLabel
                    direction={order}
                    onClick={this.createSortHandler(row.id)}
                  >
                    {row.label}
                  </TableSortLabel>
                </Tooltip>
              </TableCell>
            );
          }, this)}
        </TableRow>
      </TableHead>
    );
  }
}

EnhancedTableHead.propTypes = {
  onRequestSort: PropTypes.func.isRequired,
  order: PropTypes.string.isRequired,
  orderBy: PropTypes.string.isRequired,
  rowCount: PropTypes.number.isRequired
};

const styles = theme => ({
  root: {
    width: "100%",
    marginTop: theme.spacing.unit * 3
  },
  table: {
    minWidth: 100
  },
  tableWrapper: {
    overflowX: "auto"
  }
});

class EnhancedTable extends React.Component {
  state = {
    order: "desc",
    orderBy: "content0",
    data: recordData,
    page: 0,
    rowsPerPage: recordData.length
  };

  handleRequestSort = (event, property) => {
    const orderBy = property;
    let order = "desc";

    this.setState({ order, orderBy });
  };

  handleChangePage = (event, page) => {
    this.setState({ page });
  };

  handleChangeRowsPerPage = event => {
    this.setState({ rowsPerPage: event.target.value });
  };

  render() {
    const { classes } = this.props;
    const { data, order, orderBy, rowsPerPage, page } = this.state;
    const emptyRows =
      rowsPerPage - Math.min(rowsPerPage, data.length - page * rowsPerPage);
    var jun = 1;
    return (
      <Paper className={classes.root}>
        <div className={classes.tableWrapper}>
          <Table className={classes.table} aria-labelledby="tableTitle">
            <EnhancedTableHead
              order={order}
              orderBy={orderBy}
              onRequestSort={this.handleRequestSort}
              rowCount={data.length}
            />
            <TableBody>
              {data.sort(getSorting(order, orderBy)).map(n => {
                return (
                  <TableRow hover tabIndex={-1} key={n.id}>
                    <TableCell numeric padding="checkbox">
                      {jun++}
                    </TableCell>
                    <TableCell component="th" scope="row" padding="none">
                      {n.name}
                    </TableCell>
                    <TableCell component="th" scope="row" padding="checkbox">
                      {n.team}
                    </TableCell>
                    <TableCell numeric>{n.content0}</TableCell>
                    <TableCell numeric>{n.content1}</TableCell>
                    <TableCell numeric>{n.content2}</TableCell>
                    <TableCell numeric>{n.content3}</TableCell>
                    <TableCell numeric>{n.content4}</TableCell>
                    <TableCell numeric>{n.content5}</TableCell>
                    <TableCell numeric>{n.content6}</TableCell>
                    <TableCell numeric>{n.content7}</TableCell>
                    <TableCell numeric>{n.content8}</TableCell>
                    <TableCell numeric>{n.content9}</TableCell>
                    <TableCell numeric>{n.content10}</TableCell>
                    <TableCell numeric>{n.content11}</TableCell>
                    <TableCell numeric>{n.content12}</TableCell>
                    <TableCell numeric>{n.content13}</TableCell>
                    <TableCell numeric>{n.content14}</TableCell>
                    <TableCell numeric>{n.content15}</TableCell>
                    <TableCell numeric>{n.content16}</TableCell>
                    <TableCell numeric>{n.content17}</TableCell>
                    <TableCell numeric>{n.content18}</TableCell>
                    <TableCell numeric>{n.content19}</TableCell>
                    <TableCell numeric>{n.content20}</TableCell>
                    <TableCell numeric>{n.content21}</TableCell>
                    <TableCell numeric>{n.content22}</TableCell>
                    <TableCell numeric>{n.content23}</TableCell>
                    <TableCell numeric>{n.content24}</TableCell>
                    <TableCell numeric>{n.content25}</TableCell>
                    <TableCell numeric>{n.content26}</TableCell>
                    <TableCell numeric>{n.content27}</TableCell>
                    <TableCell numeric>{n.content28}</TableCell>
                    <TableCell numeric>{n.content29}</TableCell>
                    <TableCell numeric>{n.content30}</TableCell>
                    <TableCell numeric>{n.content31}</TableCell>
                    <TableCell numeric>{n.content32}</TableCell>
                    <TableCell numeric>{n.content33}</TableCell>
                    <TableCell numeric>{n.content34}</TableCell>
                    <TableCell numeric>{n.content35}</TableCell>
                    <TableCell numeric>{n.content36}</TableCell>
                    <TableCell numeric>{n.content37}</TableCell>
                    <TableCell numeric>{n.content38}</TableCell>
                    <TableCell numeric>{n.content39}</TableCell>
                    <TableCell numeric>{n.content40}</TableCell>
                    <TableCell numeric>{n.content41}</TableCell>
                    <TableCell numeric>{n.content42}</TableCell>
                    <TableCell numeric>{n.content43}</TableCell>
                    <TableCell numeric>{n.content44}</TableCell>
                    <TableCell numeric>{n.content45}</TableCell>
                    <TableCell numeric>{n.content46}</TableCell>
                    <TableCell numeric>{n.content47}</TableCell>
                    <TableCell numeric>{n.content48}</TableCell>
                    <TableCell numeric>{n.content49}</TableCell>
                  </TableRow>
                );
              })}
              {emptyRows > 0 && (
                <TableRow style={{ height: 49 * emptyRows }}>
                  <TableCell colSpan={6} />
                </TableRow>
              )}
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
