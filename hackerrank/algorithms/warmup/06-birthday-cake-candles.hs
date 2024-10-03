import Control.Applicative
import Control.Monad
import System.IO


main :: IO ()
main = do
    n_temp <- getLine
    let n = read n_temp :: Int
    ar_temp <- getLine
    let ar = map read $ words ar_temp :: [Int]
    putStr $ show $ countmax ar 0 0

countmax :: [Int] -> Int -> Int -> Int
countmax (x:xs) mx cnt | x > mx = countmax xs x 1
                       | x < mx = countmax xs mx cnt
                       | otherwise = countmax xs mx (cnt + 1)
countmax [] mx cnt = cnt
