import Control.Applicative
import Control.Monad
import System.IO


main :: IO [()]
main = do
    n_temp <- getLine
    let n = read n_temp :: Int
    mapM putStrLn (stair n n)

stair :: Int -> Int -> [String]
stair 0 _ = [""]
stair n 1 = (step n 1):[]
stair n i = (step n i) : stair n (i-1)

step :: Int -> Int -> String
step n i = [str | let str = ' ', i<-[1..(i-1)]] ++
           [str | let str = '#', i<-[1..(n-i+1)]]
