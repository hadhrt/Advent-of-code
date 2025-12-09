use std::fs::File;
use std::io::prelude::*;
use std::time::{SystemTime, UNIX_EPOCH};

fn part1(lines: &Vec<&str>) -> i32 {
    let mut number_of_zero_pos = 0;
    let mut dial_position = 50;
    for line in lines {
        match &line[..1] {
            "R" => {
                dial_position = (dial_position + line[1..].parse::<i32>().expect("invalid number "))
                    .rem_euclid(100)
            }
            "L" => {
                dial_position = (dial_position - line[1..].parse::<i32>().expect("invalid number "))
                    .rem_euclid(100)
            }
            _ => println!("invalid line: {}", line),
        }
        // println!("dial Position: {}", dial_position);
        if dial_position == 0 {
            number_of_zero_pos += 1
        }
    }
    number_of_zero_pos
}

fn part2(lines: &Vec<&str>) -> i32 {
    let mut number_of_zero_pos = 0;
    let mut dial_position = 50;

    for line in lines {
        let mut rotation_value = line[1..].parse::<i32>().expect("invalid number ");
        match &line[..1] {
            "R" => {
                // full rotations
                number_of_zero_pos += rotation_value / 100;
                rotation_value = rotation_value.rem_euclid(100);
                
                // remaining partial rotation to consider            
                dial_position += rotation_value;
//                number_of_zero_pos += dial_position / 100;
                if dial_position >= 100 {
                    number_of_zero_pos += 1
                }
                dial_position = dial_position.rem_euclid(100);
            }
            "L" => {
                // full rotations
                number_of_zero_pos += rotation_value / 100;
                rotation_value = rotation_value.rem_euclid(100);

                // remaining partial rotation to consider only if dial was not at 0
                if dial_position != 0 {
                    dial_position -= rotation_value;
                    if dial_position <= 0 {
                        number_of_zero_pos += 1;
                    dial_position = dial_position.rem_euclid(100);    
                    }
                }
                else {
                    dial_position = (dial_position - rotation_value).rem_euclid(100);

                }
            }
            _ => println!("invalid line: {}", line),
        }
    }
    number_of_zero_pos
}

fn main() {
    //let mut file = File::open("./../../Inputs/example.input").expect("Faild to read InputFile");
    let mut file = File::open("./../../Inputs/01.input").expect("Faild to read InputFile");
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
