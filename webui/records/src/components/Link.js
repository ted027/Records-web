import React from 'react';
import PropTypes from 'prop-types';

const Link = ({ children, onClick }) => {
    <a href="#">{children}</a>
}

Link.propTypes = {
    children: PropTypes.node.isRequired
}

export default Link