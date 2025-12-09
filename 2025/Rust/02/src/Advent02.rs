use std::fs::File;
use std::io::prelude::*;
use std::time::{SystemTime, UNIX_EPOCH};

fn part1(lines: &Vec<&str>) -> i32 {
    let mut final_value = 0;

    for line in lines {
        let range_strings: Vec<&str> = line.split(",").collect();
        for range_string in range_strings{
            if let Some((range_start,range_end)) = range_string.split_once("-"){
                for i in range_start.parse().expect("invalid range")..range_endrange_start.parse().expect("invalid range") {
                    if i.parse(&str).len() %2 == 0 {
                        if i.parse(&str)[..i.parse(&str).len()/2] == i.parse(&str)[i.parse(&str).len()/2..]{
                           final_value += 1 
                        }

                    }
                }
            }
        }
    }
    final_value
}

fn part2(lines: &Vec<&str>) -> i32 {
    let mut final_value = 0;
    for line in lines {
        match &line[..] {
            "1" => {
                final_value += 1
            }
            _ => println!("invalid line: {}", line),
        }
    }
    final_value
}

fn main() {
    let mut file = File::open("./../../Inputs/example.input").expect("Faild to read InputFile");
    //let mut file = File::open("./../../Inputs/01.input").expect("Faild to read InputFile");
    let mut contents = String::new();
    file.read_to_string(&mut contents)
        .expect("Failed to convert Input File");
    let lines = contents.lines().collect::<Vec<&str>>();

    // Part 1
    let start = SystemTime::now().duration_since(UNIX_EPOCH).unwrap();
    let result_p1 = part1(&lines);
    let end = SystemTime::now().duration_since(UNIX_EPOCH).unwrap();
    let duration_p1 = end - start;
    println!("Result Part1: {}", result_p1);
    println!(
        "Time   Part1: {:.4} sec",
        (duration_p1.as_millis() as f32) / 1000.0
    );

    // Part 2
    let start = SystemTime::now().duration_since(UNIX_EPOCH).unwrap();
    let result_p1 = part2(&lines);
    let end = SystemTime::now().duration_since(UNIX_EPOCH).unwrap();
    let duration_p1 = end - start;
    println!("Result Part2: {}", result_p1);
    println!(
        "Time   Part2: {:.4} sec",
        (duration_p1.as_millis() as f32) / 1000.0
    );
}