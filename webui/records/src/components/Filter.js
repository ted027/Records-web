import React from 'react';
import Link from './Link';

const Filter=()=>(
    <p>
        Show:
        {""}
        <Link>
            All
        </Link>
        {","}
        <Link>
            Active
        </Link>
        {","}
        <Link>
            Completed
        </Link>
    </p>
)
export default Filter