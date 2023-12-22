const Frame = ({children}) => {

    return (
    <div class="h-auto w-screen bg-slate-300 relative flex overflow-hidden">
      <div class="w-screen h-auto justify-between">
        {children}
      </div>
    </div>   
    )

}

export default Frame;