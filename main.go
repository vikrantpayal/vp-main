package main

import (
    "fmt"
    // "encoding/csv"
    // "log"
    "os"
)

func main(){
    fmt.Println("Hello")
    process_bank_statement()
}


func process_bank_statement(){
    open_file_csv()
    read_file()
}

func open_file_csv(){
    file, err := os.Open("data.csv")
    if err != nil{
        log.Fatalf("Failed to open CSV : %s", err)
    }

    defer file.Close()
}

func read_file(){
}

