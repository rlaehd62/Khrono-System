import React, { useEffect, useState } from 'react';
import { createClient } from '@supabase/supabase-js'

const supabaseKey = process.env.REACT_APP_KEY
const supabaseUrl = process.env.REACT_APP_URL
const supabase = createClient(supabaseUrl, supabaseKey)

const NewsInfo = ({TYPE}) => {

    const [news, setNews] = useState([])

    const load = async() => {
        let { data, error } = await supabase
            .from('News')
            .select('*')
            .eq('TYPE', TYPE)
            .order('SYNC', { ascending: false })
            .limit(15)
        setNews(data)
    }

    useEffect(() => {

        const temp = async() => {
            await load()
        }

        temp()
    }, []);

    return (
        <div className='mx-4'>
            {
                news.map((data) => (
                    <div className='flex flex-col bg-slate-100 my-5 rounded-lg px-3 py-5'>
                        <div className='font-bold'>{data.DATE.substring(0, 4)}년 {data.DATE.substring(4, 6)}월 기사</div>
                        <div className='w-60 truncate'><a className='nav-item' href={data.URL || 'https://google.com/search?q=' + data.TITLE }>{data.TITLE}</a></div>
                        <div className='italic'>{Math.fround(data.SYNC) * 100} (%) &nbsp;&nbsp;</div>
                    </div>
                ))
            }
        </div>
    )
}

export default NewsInfo;