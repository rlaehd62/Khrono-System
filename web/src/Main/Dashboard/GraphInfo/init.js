import React, { useEffect, useState } from 'react';
import { createClient } from '@supabase/supabase-js'

const supabaseKey = process.env.REACT_APP_KEY
const supabaseUrl = process.env.REACT_APP_URL
const supabase = createClient(supabaseUrl, supabaseKey)

const GraphInfo = () => {

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
            {
                economy.map((data) => (
                    <div>
                        <div>{data.TYPE}</div>
                        <div>{data.DATE}</div>
                        <div>{Math.fround(data.SYNC) * 100}% &nbsp;&nbsp;</div>
                        <br />
                    </div>
                ))
            }
            
            {
                science.map((data) => (
                    <div>
                        <div>{data.TYPE}</div>
                        <div>{data.DATE}</div>
                        <div>{Math.fround(data.SYNC) * 100}% &nbsp;&nbsp;</div>
                        <br />
                    </div>
                ))
            }
        </div>
    )
}

export default GraphInfo;