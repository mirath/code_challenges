import Control.Applicative
import Control.Monad
import System.IO

main :: IO ()
main = do
    a0_temp <- getLine
    let a0_t = words a0_temp
    let a0 = read $ a0_t!!0 :: Int
    let a1 = read $ a0_t!!1 :: Int
    let a2 = read $ a0_t!!2 :: Int
    b0_temp <- getLine
    let b0_t = words b0_temp
    let b0 = read $ b0_t!!0 :: Int
    let b1 = read $ b0_t!!1 :: Int
    let b2 = read $ b0_t!!2 :: Int
    let ret = solve a0 a1 a2 b0 b1 b2
    putStr $ show $ ret!!0
    putStr " "
    putStr $ show $ ret!!1

solve :: Int -> Int -> Int -> Int -> Int -> Int -> [Int]
solve a0 a1 a2 b0 b1 b2 = [(tester a0 b0) + (tester a1 b1) + (tester a2 b2),
                           (tester b0 a0) + (tester b1 a1) + (tester b2 a2)]

tester :: Int -> Int -> Int
tester a b | a > b     = 1
           | otherwise = 0
