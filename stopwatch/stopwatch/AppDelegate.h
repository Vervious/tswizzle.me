//
//  AppDelegate.h
//  stopwatch
//
//  Created by Benjamin Y Chan on 1/17/15.
//  Copyright (c) 2015 tswizzle. All rights reserved.
//

#import <Cocoa/Cocoa.h>

@interface AppDelegate : NSObject <NSApplicationDelegate>

@property (nonatomic, weak) IBOutlet NSTextField *timeElapsedView;
@property (nonatomic, strong) IBOutlet NSTextView *stopwatchPreview;

- (IBAction)startTime:(id)sender;
- (IBAction)resetTime:(id)sender;
- (IBAction)noteTime:(id)sender;

@end

