import { connect } from 'react-redux';
import TodoList from '../components/TodoList'

const mapStateToProps = (state) => {
    return { todos: state }
}

const VisibleTodoList = connect(
    mapStateToProps
)(TodoList)

export default VisibleTodoList