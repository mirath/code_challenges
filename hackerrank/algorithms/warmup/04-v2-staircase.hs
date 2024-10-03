import Control.Applicative
import Control.Monad
import System.IO


main :: IO ()
main = do
    n_temp <- getLine
    let n = read n_temp :: Int
    stair n n

stair :: Int -> Int -> IO ()
stair _ 0 = putStr ""
stair n i = putStrLn (step n i) >> (stair n (i-1))

step :: Int -> Int -> String
step n i = (take (i-1) (repeat ' ')) ++ (take (n-i+1) (repeat '#'))
