import React, { useEffect, useState } from 'react';
import { createClient } from '@supabase/supabase-js'
import Graph from './Graph/init'

const supabaseKey = process.env.REACT_APP_KEY
const supabaseUrl = process.env.REACT_APP_URL
const supabase = createClient(supabaseUrl, supabaseKey)

const GraphInfo = () => {

    const [labels, setLabels] = useState([])
    const [economy, setEconomy] = useState([])
    const [science, setScience] = useState([])

    const load = async(TYPE, Setter) => {
        let { data, error } = await supabase
            .from('Sync')
            .select('*')
            .eq('TYPE', TYPE)
            .order('DATE', { ascending: true })
        Setter(data)
    }

    useEffect(() => {

        const temp = async() => {
            await load('ECONOMY', setEconomy)
            await load('SCIENCE', setScience)

        }
        
        temp()

    }, []);

    return (
        <div className='mx-2'>
            <Graph labels={economy.map(data => data.DATE.substring(4, 6)+'월')} economy={economy} science={science} />
        </div>
    )
}

export default GraphInfo;