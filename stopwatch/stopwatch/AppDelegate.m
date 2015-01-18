//
//  AppDelegate.m
//  stopwatch
//
//  Created by Benjamin Y Chan on 1/17/15.
//  Copyright (c) 2015 tswizzle. All rights reserved.
//

#import "AppDelegate.h"

@interface AppDelegate () {
    NSTimeInterval startTime;
    NSTimer *updater;
    NSFileHandle *fileHandle;
}

@property (weak) IBOutlet NSWindow *window;
@end

@implementation AppDelegate

- (void)applicationDidFinishLaunching:(NSNotification *)aNotification {
    // Insert code here to initialize your application
    /*NSString *dataPath = [[NSBundle mainBundle] pathForResource:@"saved" ofType:@"txt"];
    NSFileHandle* fh = [NSFileHandle fileHandleForWritingAtPath:dataPath];
    if ( !fh ) {
        [[NSFileManager defaultManager] createFileAtPath:dataPath contents:nil attributes:nil];
        fh = [NSFileHandle fileHandleForWritingAtPath:dataPath];
    }
    fileHandle = fh;*/
}

- (void)applicationWillTerminate:(NSNotification *)aNotification {
    // Insert code here to tear down your application
    [updater invalidate];
    NSString *contents = [self.stopwatchPreview string];
    NSError *err = nil;
    NSString *dataPath = [[NSBundle mainBundle] pathForResource:@"saved" ofType:@"txt"];
    if(![contents writeToFile:dataPath atomically:YES encoding:NSUTF8StringEncoding error:&err]) {
        NSLog(@"Writing failed with err: %@", err);
    }
    //[fileHandle closeFile];
    updater = nil;
}

- (void)updateTimeView {
    [self.timeElapsedView setStringValue:[NSString stringWithFormat:@"%g", [self timeElapsed]]];
}

- (NSTimeInterval) timeElapsed {
    NSTimeInterval currentTime = [NSDate timeIntervalSinceReferenceDate];
    return currentTime - startTime;
}

- (IBAction)startTime:(id)sender {
    startTime = [NSDate timeIntervalSinceReferenceDate];
    
    updater = [NSTimer scheduledTimerWithTimeInterval:1.0
                                               target:self
                                             selector:@selector(updateTimeView)
                                             userInfo:nil
                                              repeats:YES];
}

- (IBAction)resetTime:(id)sender {
    startTime = [NSDate timeIntervalSinceReferenceDate];
    [self.stopwatchPreview setString:@""];
}

- (IBAction)noteTime:(id)sender {
    [[self.stopwatchPreview textStorage] appendAttributedString:[[NSAttributedString alloc] initWithString:[NSString stringWithFormat:@"%g, ", [self timeElapsed]]]];
}

// unused
//- (BOOL) appendString:(NSString *)string encoding:(NSStringEncoding)enc;
//{
//    BOOL result = YES;
//
//    if ( !fileHandle ) return NO;
//    @try {
//        [fileHandle seekToEndOfFile];
//        [fileHandle writeData:[string dataUsingEncoding:enc]];
//    }
//    @catch (NSException * e) {
//        result = NO;
//    }
//    return result;
//}

@end
