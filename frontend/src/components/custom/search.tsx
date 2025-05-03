import { Search } from "lucide-react"
import { Input } from "../ui/input"
import { Button } from "../ui/button"

const SearchBox = () => {
    return (
        <div className="flex items-center justify-between gap-2 mt-12 px-12">
            <div className="relative w-full">
                <Search className="absolute top-1/2 left-2 -translate-y-1/2" size={16}/>
                <Input type="text" placeholder="Search todo..." className="pl-8"/>
            </div>
            <Button className="cursor-pointer bg-primary">Search</Button>
        </div>
    )
}

export default SearchBox