import GraphInfo from "./GraphInfo/init";
import NewsInfo from "./NewsInfo/init";


const Dashboard = () => {
    return(
        <div class="flex justify-center flex-wrap h-auto py-4 my-4 gap-x-6">

            <div class="basis-2/4 h-scren rounded bg-slate-200">
                <GraphInfo />
            </div>

            {/* 경제 뉴스 */}
            <div class="basis-1/5 h-scren rounded bg-slate-200">
                <h3 className="my-1 text-center font-bold text-2xl">경제</h3>
                <NewsInfo TYPE="ECONOMY" />
            </div>

            
            {/* 과학 뉴스 */}
            <div class="basis-1/5 h-scren rounded bg-slate-200">
                <h3 className="my-1 text-center font-bold text-2xl">과학</h3>
                <NewsInfo TYPE="SCIENCE" />
            </div>
        </div>
    )
}

export default Dashboard;