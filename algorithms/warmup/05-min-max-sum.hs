import Control.Applicative
import Control.Monad
import System.IO
import Data.List

main :: IO ()
main = do
    arr_temp <- getLine
    let arr = map read $ words arr_temp :: [Int]
    putStr (show (minsum2 arr))
    putStr " "
    putStr (show (maxsum2 arr))

-- Using built-in functions
maxsum xs = (sum xs) - (minimum xs)
minsum xs = (sum xs) - (maximum xs)

-- Sorting the lists and taking the sum of the first 4 elements
maxsum2 xs = sum $ take 4 $ (sortBy (flip compare)) xs
minsum2 xs = sum $ take 4 $ sort xs
