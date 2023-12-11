const Header = ({msg}) => {

    return (
        <header class="h-16 w-full flex items-center relative justify-end px-5 space-x-10 bg-blue-700">
          <div class="flex flex-shrink-0 items-center space-x-4 text-white">
            <div class="flex flex-col items-end ">
              <div class="text-md font-medium font-bold">Khrono System</div>
              <div class="text-sm font-regular font-bold">김동주 (2021428782)</div>
            </div>
          </div>
        </header>
    )
}

export default Header;